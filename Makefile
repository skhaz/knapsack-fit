.PHONY: help run tests upgrade vet

.SILENT:

SHELL := bash -eou pipefail

export PYTHONPATH=.

help:
	awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

run: ## Run the project using docker-compose
	python app/main.py

tests: vet ## Run tests
	pytest --cov=app tests/

upgrade: ## Upgrade dependencies
	pur --requirement requirements/base.txt
	pur --requirement requirements/development.txt
	pur --requirement requirements/tests.txt
	pur --requirement requirements/types.txt

vet: ## Run linters, type-checking, auto-formaters, and other tools
	bandit -r app/ tests/
	black app/ tests/
	flake8 --max-line-length=88 app/ tests/
	isort --force-single-line-imports app/ tests/
