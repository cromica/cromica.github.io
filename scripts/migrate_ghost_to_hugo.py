#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import shutil
import tarfile
from collections import defaultdict
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
GHOST_EXPORT = ROOT / "migration-data/phase0/raw/ghost-admin.json"
GHOST_IMAGES_ARCHIVE = ROOT / "migration-data/phase0/raw/ghost-content-images.tar.gz"
NGINX_ARCHIVE = ROOT / "migration-data/phase0/raw/nginx-sites.tar.gz"

CONTENT_DIR = ROOT / "content"
POSTS_DIR = CONTENT_DIR / "posts"
STATIC_DIR = ROOT / "static"
STATIC_IMAGES_DIR = STATIC_DIR / "images"
REDIRECT_BLOG_DIR = STATIC_DIR / "blog"
REPORT_DIR = ROOT / "migration-data/phase2/reports"

SITE_HOST = "romuluscrisan.com"
SITE_HOST_ALIASES = (SITE_HOST, f"www.{SITE_HOST}")
IMAGE_PREFIX = "/content/images/"
IMAGE_OUTPUT_PREFIX = "/images/"
IMAGE_SUFFIXES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
}


def main() -> int:
    export = json.loads(GHOST_EXPORT.read_text())
    data = export["db"][0]["data"]

    posts = data["posts"]
    tags = {tag["id"]: tag for tag in data["tags"]}
    posts_by_id = {post["id"]: post for post in posts}

    tags_by_post_id: dict[str, list[dict]] = defaultdict(list)
    for relation in data["posts_tags"]:
        post = posts_by_id.get(relation["post_id"])
        tag = tags.get(relation["tag_id"])
        if post and tag and post["status"] == "published":
            tags_by_post_id[post["id"]].append(tag)

    page_targets = {canonical_content_path(f"/{post['slug']}/") for post in posts if post["status"] == "published"}
    redirect_map = parse_redirect_map()
    link_map, aliases_by_target = build_link_map(page_targets, redirect_map)

    unresolved_links: set[str] = set()
    written_files: list[str] = []

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    generated_post_paths = set()

    for post in sorted(posts, key=lambda item: item["published_at"]):
        if post["status"] != "published":
            continue

        target_path = canonical_content_path(f"/{post['slug']}/")
        aliases = sorted(aliases_by_target.get(target_path, set()))
        body = rewrite_content(extract_body(post), link_map, unresolved_links)
        description = build_post_description(post)
        feature_image = rewrite_asset_path(post.get("feature_image"))
        front_matter = {
            "title": post["title"],
            "date": post["published_at"],
            "lastmod": post["updated_at"],
            "slug": post["slug"],
            "description": description,
            "tags": sorted(tag["name"] for tag in tags_by_post_id.get(post["id"], [])),
            "aliases": aliases,
            "featured": bool(post.get("featured")),
            "featured_image": feature_image,
            "ghost_id": post["id"],
            "migration_source": "ghost",
        }

        if post.get("meta_title") and post["meta_title"] != post["title"]:
            front_matter["seo_title"] = post["meta_title"]

        if post.get("page"):
            output_path = CONTENT_DIR / f"{post['slug']}.md"
        else:
            output_path = POSTS_DIR / f"{post['slug']}.md"
            generated_post_paths.add(output_path)

        write_markdown(output_path, front_matter, body)
        written_files.append(str(output_path.relative_to(ROOT)))

    remove_stale_generated_posts(generated_post_paths)
    extract_images_archive()
    write_section_content(data["settings"])
    write_blog_redirect()

    image_count = count_static_images()
    alias_count = sum(len(value) for value in aliases_by_target.values())
    report = {
        "ghost_version": export["db"][0]["meta"]["version"],
        "published_posts": sum(1 for post in posts if post["status"] == "published" and not post.get("page")),
        "published_pages": sum(1 for post in posts if post["status"] == "published" and post.get("page")),
        "tag_count": len(data["tags"]),
        "redirect_alias_count": alias_count,
        "static_image_count": image_count,
        "generated_files": written_files,
        "unresolved_internal_links": sorted(unresolved_links),
    }
    write_report(report)

    print(
        f"Migrated {report['published_posts']} posts, {report['published_pages']} pages, "
        f"{report['static_image_count']} images, {report['redirect_alias_count']} aliases."
    )
    if unresolved_links:
        print(f"Unresolved internal links: {len(unresolved_links)}")
    return 0


def first_non_empty(*values: str | None) -> str | None:
    for value in values:
        if value:
            stripped = value.strip()
            if stripped:
                return stripped
    return None


def build_post_description(post: dict) -> str | None:
    return first_non_empty(
        normalize_description(post.get("custom_excerpt")),
        normalize_description(post.get("meta_description")),
    )


def normalize_description(value: str | None) -> str | None:
    if not value:
        return None
    collapsed = re.sub(r"\s+", " ", value).strip()
    return collapsed or None


def parse_redirect_map() -> dict[str, str]:
    with tarfile.open(NGINX_ARCHIVE) as archive:
        member = next(
            (
                item
                for item in archive.getmembers()
                if item.name.endswith("sites-available/ghost")
            ),
            None,
        )
        if not member:
            return {}
        config = archive.extractfile(member).read().decode("utf-8")

    redirects: dict[str, str] = {}

    rewrite_pattern = re.compile(
        r"rewrite\s+\^?(?P<src>/\S+?)\s+(?P<dest>/\S+?)(?:\s+permanent)?;",
        re.MULTILINE,
    )
    for match in rewrite_pattern.finditer(config):
        src = normalize_source_path(match.group("src"))
        dest = canonical_content_path(match.group("dest"))
        redirects[src] = dest

    location_pattern = re.compile(
        r"location\s+'(?P<src>[^']+)'\s*\{\s*return\s+301\s+\$scheme://\$host(?P<dest>/[^;]+);",
        re.MULTILINE,
    )
    for match in location_pattern.finditer(config):
        src = normalize_source_path(match.group("src"))
        dest = canonical_content_path(match.group("dest"))
        redirects[src] = dest

    redirects["/blog/"] = "/"
    return redirects


def normalize_source_path(path: str) -> str:
    path = path.strip().replace("^", "")
    if not path.startswith("/"):
        path = f"/{path}"
    path = re.sub(r"/{2,}", "/", path)
    if " " in path:
        path = quote(path, safe="/.-_~#%")
    return path


def build_link_map(page_targets: set[str], redirect_map: dict[str, str]) -> tuple[dict[str, str], dict[str, set[str]]]:
    link_map: dict[str, str] = {}
    aliases_by_target: dict[str, set[str]] = defaultdict(set)

    for page_target in sorted(page_targets):
        plain = page_target.rstrip("/") or "/"
        candidates = {page_target, plain}
        for host in SITE_HOST_ALIASES:
            candidates.add(f"https://{host}{page_target}")
            candidates.add(f"http://{host}{page_target}")
        for candidate in candidates:
            link_map[candidate] = page_target

    link_map["/"] = "/"
    link_map["/index.html"] = "/"

    for source, destination in redirect_map.items():
        if destination not in page_targets and destination != "/":
            continue
        aliases_by_target[destination].add(source)
        for variant in redirect_source_variants(source):
            link_map[variant] = destination
            if variant.startswith("/"):
                for host in SITE_HOST_ALIASES:
                    link_map[f"https://{host}{variant}"] = destination
                    link_map[f"http://{host}{variant}"] = destination

    return link_map, aliases_by_target


def redirect_source_variants(source: str) -> set[str]:
    variants = {source, unquote(source), quote(unquote(source), safe="/.-_~#%")}
    if source != "/":
        if source.endswith("/"):
            trimmed = source.rstrip("/")
            variants.update({trimmed, unquote(trimmed), quote(unquote(trimmed), safe="/.-_~#%")})
        else:
            trailed = f"{source}/"
            variants.update({trailed, unquote(trailed), quote(unquote(trailed), safe="/.-_~#%")})
    return {variant for variant in variants if variant}


def extract_body(post: dict) -> str:
    mobiledoc = post.get("mobiledoc")
    if mobiledoc:
        document = json.loads(mobiledoc)
        parts = []
        for card in document.get("cards", []):
            if card[0] == "card-markdown":
                markdown = card[1].get("markdown", "").strip()
                if markdown:
                    parts.append(markdown)
        if parts:
            return cleanup_markdown("\n\n".join(parts))

    html = (post.get("html") or "").strip()
    return cleanup_markdown(html)


def cleanup_markdown(body: str) -> str:
    body = body.replace("\r\n", "\n").strip()
    body = re.sub(r"^(#{1,6})([^\s#])", r"\1 \2", body, flags=re.MULTILINE)
    body = re.sub(r"^(#{1,6})\s*(.*?)\s*#+\s*$", r"\1 \2", body, flags=re.MULTILINE)
    return body


def rewrite_content(body: str, link_map: dict[str, str], unresolved_links: set[str]) -> str:
    body = body.replace(IMAGE_PREFIX, IMAGE_OUTPUT_PREFIX)
    for host in SITE_HOST_ALIASES:
        body = body.replace(f"https://{host}{IMAGE_PREFIX}", IMAGE_OUTPUT_PREFIX)
        body = body.replace(f"http://{host}{IMAGE_PREFIX}", IMAGE_OUTPUT_PREFIX)
    body = normalize_scheme_less_external_links(body)

    host_pattern = "|".join(re.escape(host) for host in SITE_HOST_ALIASES)
    absolute_site_pattern = re.compile(rf"https?://(?:{host_pattern})[^\s)\"'>]+")

    def replace_absolute_site_link(match: re.Match[str]) -> str:
        original = match.group(0)
        parsed = urlparse(original)
        path = parsed.path or "/"
        fragment = f"#{parsed.fragment}" if parsed.fragment else ""
        query = f"?{parsed.query}" if parsed.query else ""

        if path == "/index.html" and parsed.fragment == "contact":
            return "/contact/"

        if path.startswith(IMAGE_PREFIX):
            return f"{rewrite_asset_path(path)}{query}{fragment}"

        candidates = lookup_variants(original, path)
        for candidate in candidates:
            if candidate in link_map:
                mapped = link_map[candidate]
                return f"{mapped}{query}{fragment}"

        unresolved_links.add(original)
        return original

    return absolute_site_pattern.sub(replace_absolute_site_link, body).strip() + "\n"


def normalize_scheme_less_external_links(body: str) -> str:
    html_pattern = re.compile(r'(?P<prefix>href=["\'])(?P<url>(?!https?://|mailto:|/|#)[^"\'\s>]+)')
    markdown_pattern = re.compile(r'(?P<prefix>\]\()(?P<url>(?!https?://|mailto:|/|#)[^\s)]+)')

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if not looks_like_external_url(url):
            return match.group(0)
        return f"{match.group('prefix')}https://{url}"

    body = html_pattern.sub(replace, body)
    body = markdown_pattern.sub(replace, body)
    return body


def looks_like_external_url(url: str) -> bool:
    candidate = url.lstrip("<").rstrip(".,;:!?)>").lower()
    if "." not in candidate:
        return False
    first_segment = candidate.split("/", 1)[0]
    return "." in first_segment


def normalize_alias_lookup(path: str) -> str:
    decoded = unquote(path)
    if decoded != "/" and not Path(decoded).suffix and not decoded.endswith("/"):
        return f"{decoded}/"
    return decoded


def lookup_variants(original: str, path: str) -> list[str]:
    variants = [
        original,
        path,
        unquote(path),
        normalize_alias_lookup(path),
        quote(unquote(path), safe="/.-_~#%"),
    ]
    if path != "/" and not path.endswith("/"):
        variants.append(f"{path}/")
        variants.append(f"{unquote(path)}/")
        variants.append(quote(f"{unquote(path)}/", safe="/.-_~#%"))
    return variants


def canonical_content_path(path: str | None) -> str | None:
    if not path:
        return None
    parsed = urlparse(path)
    candidate = parsed.path or parsed.netloc or path
    if not candidate.startswith("/"):
        candidate = f"/{candidate}"
    candidate = re.sub(r"/{2,}", "/", candidate)
    if candidate != "/" and not Path(candidate).suffix and not candidate.endswith("/"):
        candidate = f"{candidate}/"
    return candidate


def rewrite_asset_path(path: str | None) -> str | None:
    if not path:
        return None
    for host in SITE_HOST_ALIASES:
        path = path.replace(f"https://{host}", "").replace(f"http://{host}", "")
    if path.startswith(IMAGE_PREFIX):
        return path.replace(IMAGE_PREFIX, IMAGE_OUTPUT_PREFIX, 1)
    return path


def write_markdown(path: Path, front_matter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["+++"]
    for key, value in front_matter.items():
        if value in (None, "", [], {}):
            continue
        lines.extend(render_toml_value(key, value))
    lines.append("+++")
    lines.append("")
    path.write_text("\n".join(lines) + body)


def render_toml_value(key: str, value) -> Iterable[str]:
    if isinstance(value, bool):
        return [f"{key} = {str(value).lower()}"]
    if isinstance(value, list):
        encoded = ", ".join(json.dumps(item, ensure_ascii=False) for item in value)
        return [f"{key} = [{encoded}]"]
    if isinstance(value, str) and looks_like_datetime(value):
        return [f"{key} = {value}"]
    return [f"{key} = {json.dumps(value, ensure_ascii=False)}"]


def looks_like_datetime(value: str) -> bool:
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$", value))


def remove_stale_generated_posts(generated_post_paths: set[Path]) -> None:
    for markdown_file in POSTS_DIR.glob("*.md"):
        if markdown_file.name == "_index.md":
            continue
        if markdown_file in generated_post_paths:
            continue
        content = markdown_file.read_text()
        if 'migration_source = "ghost"' in content:
            markdown_file.unlink()


def extract_images_archive() -> None:
    if STATIC_IMAGES_DIR.exists():
        shutil.rmtree(STATIC_IMAGES_DIR)
    STATIC_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    with tarfile.open(GHOST_IMAGES_ARCHIVE) as archive:
        for member in archive.getmembers():
            member_path = Path(member.name)
            if not member.isfile() or member_path.suffix.lower() not in IMAGE_SUFFIXES:
                continue
            if not member.name.startswith("images/"):
                continue

            destination = STATIC_DIR / member.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as src, destination.open("wb") as dst:
                shutil.copyfileobj(src, dst)


def count_static_images() -> int:
    return sum(1 for path in STATIC_IMAGES_DIR.rglob("*") if path.is_file())


def write_section_content(settings: list[dict]) -> None:
    settings_map = {item["key"]: item.get("value") for item in settings}
    title = settings_map.get("title") or "Home"
    description = settings_map.get("description")

    home_lines = ["+++", f"title = {json.dumps(title, ensure_ascii=False)}"]
    if description:
        home_lines.append(f"description = {json.dumps(description, ensure_ascii=False)}")
    home_lines.extend(["+++", ""])
    if description:
        home_lines.append(description)
        home_lines.append("")
    (CONTENT_DIR / "_index.md").write_text("\n".join(home_lines))

    posts_lines = ["+++", 'title = "Posts"', "+++", ""]
    (POSTS_DIR / "_index.md").write_text("\n".join(posts_lines))


def write_blog_redirect() -> None:
    REDIRECT_BLOG_DIR.mkdir(parents=True, exist_ok=True)
    redirect_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=/">
    <link rel="canonical" href="/">
    <title>Redirecting…</title>
  </head>
  <body>
    <p>Redirecting to <a href="/">the homepage</a>.</p>
  </body>
</html>
"""
    (REDIRECT_BLOG_DIR / "index.html").write_text(redirect_html)


def write_report(report: dict) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "content-migration-report.json").write_text(json.dumps(report, indent=2) + "\n")

    summary_lines = [
        "Ghost → Hugo content migration",
        f"Ghost version: {report['ghost_version']}",
        f"Published posts: {report['published_posts']}",
        f"Published pages: {report['published_pages']}",
        f"Tags captured: {report['tag_count']}",
        f"Redirect aliases generated: {report['redirect_alias_count']}",
        f"Static images extracted: {report['static_image_count']}",
        f"Unresolved internal links: {len(report['unresolved_internal_links'])}",
    ]
    if report["unresolved_internal_links"]:
        summary_lines.extend(["", "Unresolved links:"])
        summary_lines.extend(f"- {item}" for item in report["unresolved_internal_links"])

    (REPORT_DIR / "content-migration-summary.txt").write_text("\n".join(summary_lines) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
