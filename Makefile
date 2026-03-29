.PHONY: build migrate serve check-hugo-version

HUGO_VERSION := $(shell cat .hugo-version)

build: check-hugo-version
	hugo --gc --minify

migrate:
	python3 scripts/migrate_ghost_to_hugo.py

serve: check-hugo-version
	hugo server -D

check-hugo-version:
	@./scripts/check-hugo-version.sh "$(HUGO_VERSION)"
