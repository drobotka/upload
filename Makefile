# upload — Layer-0 asset repo (public). `make verify` is the one merge-gate.
SHELL := /bin/bash
PY := python3

.DEFAULT_GOAL := help
.PHONY: help verify gate-cruft gate-json gate-assets manifest

help: ## Show available targets
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
	  | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

verify: gate-cruft gate-json gate-assets ## Run the full HARD gate suite (merge-gate)
	@echo
	@echo "== make verify: GREEN =="

gate-cruft: ## No cruft artifacts in scope (R10)
	@echo "[gate] cruft"
	@! git ls-files | grep -E '\.(orig|bak|log)$$|~$$|_PATCH_' || { echo "  cruft"; exit 1; }

gate-json: ## MANIFEST.json parses
	@echo "[gate] json"
	@$(PY) -c "import json; json.load(open('brand/MANIFEST.json')); print('  ok')"

gate-assets: ## PNGs valid + sizes match names + web-core contract + OG (Form->Wahrheit)
	@echo "[gate] assets"
	@$(PY) scripts/verify_assets.py

manifest: ## Regenerate brand/MANIFEST.json from the asset bytes
	@$(PY) scripts/build_manifest.py
