# Phase 0 Archive Validation Pattern

**Purpose:** Verify content capture archives are complete and valid without full extraction.

**When to use:** After Phase 0 operator completes raw capture and hands back manifests + checksums.

## Quick Validation Steps

### 1. Check Archive Integrity (No Extraction)
```bash
# List contents without extracting
tar -tzf <archive.tar.gz> | head -20

# Verify archive is not corrupted
tar -tzf <archive.tar.gz> > /dev/null && echo "VALID" || echo "CORRUPT"
```

### 2. Validate JSON Exports
```bash
# Check file exists and is non-zero
ls -lh <export.json>

# Verify JSON structure without full load
jq '.db[0] | keys' <export.json> | head -20

# Count records in key tables
jq '.db[0].data.posts | length' <export.json>
jq '.db[0].data.tags | length' <export.json>

# Check metadata (version, export timestamp)
jq '.db[0].meta' <export.json>
```

### 3. Validate Checksum Manifest
```bash
# Verify all checksums pass
sha256sum -c <phase0-sha256.txt>

# Count verified files
sha256sum -c <phase0-sha256.txt> | grep -c "OK"
```

### 4. Cross-Check Evidence
**Example:** Routes/redirects may not be YAML files in all Ghost deployments.

Check for routing evidence in this order:
1. Filesystem: Look for `routes.yaml`, `redirects.yaml`, `redirects.json` in captured config
2. Nginx proxy: Extract archived Nginx configs; look for rewrite rules, upstream targets
3. Database: Check Ghost JSON `settings` table for routing/redirect data
4. Config file: Check `config.production.json` for custom routing keys

**Verdict:** If any ONE of the above contains routing evidence, routes are captured (not missing).

### 5. Size Reasonableness Check
| Archive Type | Typical Size | Red Flag |
|--|--|--|
| Nginx configs | < 10 KB | > 1 MB |
| Theme files | 50 KB – 5 MB | > 50 MB (uncompressed) |
| Images | varies | Suspiciously zero |
| DB dump (MySQL) | depends on row count | Should match remote export time |

Small archives (e.g., 3.3 KB for Nginx) are **not** data loss if:
- Archive extracts successfully
- Expected files are present
- No corruption detected

## Reusable Commands

```bash
# Full validation pipeline
validate_phase0() {
  local root="$1"
  
  # Check archive validity
  for tgz in "$root"/raw/*.tar.gz; do
    tar -tzf "$tgz" > /dev/null && echo "✓ $(basename $tgz)" || echo "✗ $(basename $tgz) CORRUPT"
  done
  
  # Verify JSON exports
  jq -e '.db[0].data.posts' "$root"/raw/ghost-admin.json > /dev/null && echo "✓ Ghost JSON valid" || echo "✗ Ghost JSON invalid"
  
  # Verify checksums
  (cd "$root" && sha256sum -c checksums/phase0-sha256.txt > /dev/null 2>&1) && echo "✓ All checksums OK" || echo "✗ Checksum mismatch"
}
```

## Common Gotchas

- **Nginx archive is tiny:** Expected for text configs on minimal Debian. Verify contents, don't assume corruption.
- **Routes not as separate YAML:** May be embedded in Ghost settings, Nginx config, or database. Check all three before declaring missing.
- **Image counts don't match exactly:** Acceptable if rsync was interrupted and re-run; check manifest for warnings.
- **JSON export lacks some tables:** Ghost exports may vary by version; check `meta.version` to understand what's expected.

## Output Format

Use this format when reporting validation results:

```
Phase 0 Archive Validation

Artifact              | Size    | Status
---------------------|---------|--------
ghost-admin.json      | 668 KB  | ✓ Valid JSON, 43 posts
ghost-content-images  | 36 MB   | ✓ Archive valid, counts match
ghost-themes.tar.gz   | 92 KB   | ✓ Active theme present
ghost-db.sql          | 663 KB  | ✓ MySQL dump, non-zero
nginx-sites.tar.gz    | 3.3 KB  | ✓ Archive valid, routing rules present
config.production.json| 611 B   | ✓ Exists (local-only)

Checksums: ✓ 5/5 verified
Routes evidence: ✓ Present (Nginx + Ghost settings)
Outstanding blockers: None

VERDICT: Phase 0 COMPLETE
```
