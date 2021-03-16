DESTINATION = '/tmp/'
REPO = 'repository-name'


.PHONY: cookie
cookie:
	@rm -rf $(DESTINATION)$(REPO)
	@cookiecutter --overwrite-if-exists --no-input -o $(DESTINATION) .
	@cd $(DESTINATION)/$(REPO); pip install -e '.[dev]'; pre-commit run --all-files ; git diff
