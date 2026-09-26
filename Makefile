.PHONY: help install demo test clean

help:
	@echo "Targets: install | demo | clean"

install:
	pip install -e .

demo:
	-python -m iac_guard fixtures/bad_nsg.tf >/tmp/iac-tf.json; test -s /tmp/iac-tf.json
	-python -m iac_guard fixtures/bad_nsg.bicep >/tmp/iac-bicep.json; test -s /tmp/iac-bicep.json
	@grep -q findings /tmp/iac-tf.json
	@echo "✓ iac-guard-mcp demo OK — findings JSON for TF + Bicep fixtures" 

clean:
	rm -rf .venv dist build *.egg-info reports labs out audit.log __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
