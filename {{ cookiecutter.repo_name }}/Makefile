VERSION := 0.0.1

.DEFAULT: help
# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help: ## Prints all commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: clean
clean: ## clean up pyc and caches
	@rm -rf */.pytest_cache/
	@rm -rf .mypy_cache/
	@rm -rf .coverage
	@find . -name '.coverage.*' -exec rm -f {} +
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: test-only
test-only: ## run tests only
	pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml --cov-report=html

.PHONY: format
format: ## run  pre-commit
	pre-commit run --all-files

.PHONY: bump_patch
bump_patch: ## Bump patch MAJOR.MINOR.PATCH
	bumpver update --patch

.PHONY: bump_minor
bump_minor: ## Bump minor MAJOR.MINOR.PATCH
	bumpver update -m

.PHONY: bump_major
bump_major: ## Bump major MAJOR.MINOR.PATCH
	bumpver update --major

.PHONY: coverage
coverage:
	coverage report --include=./*py --omit='tests/*.py' -m

.PHONY: test
test: ## run pre-commit, test and coverage
	format test-only coverage

.PHONY: dist_build
dist_build:
	python setup.py sdist bdist_wheel

.PHONY: dist_publish
dist_publish: bump_version dist_build

.PHONY: dist_release
dist_release: bump_release dist_build

.PHONY: env
env:
	pyenv virtualenv 3.8.12 {{ cookiecutter.repo_name }}
	pyenv local {{ cookiecutter.repo_name }}

.PHONY: install
install:
	pip install -e ".[dev]"

.PHONY: setup
setup: env install ## Setup the project locally

{% if cookiecutter.create_dockerfile == "y" -%}
.PHONY: docker_build
docker_build: ## Build docker image
	docker build -t {{ cookiecutter.project|lower }}/{{ cookiecutter.repo_name }}\:$(VERSION) -t {{ cookiecutter.project|lower }}/{{ cookiecutter.repo_name }}\:latest .
{%- endif %}
