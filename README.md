# Cookiecutter Data Science

The cookie-cutter template requires a few configuration parameters:

- **project**: The project that you're working on.
- **repo_name**: The DevOps repository in the project, make sure that the repository exists. Convention is to use dashes (`-`), and spaces are disallowed.
- **package_name**: Suggested package name.
- **git_url**: The github url.
- **description**: To help your fellow colleagues as an introduction to the project.

### Requirements to use the cookiecutter template:

-----------

 - Python 3.8+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

	```bash
	$ pip install cookiecutter
	```


### To start a new project, run:
------------

    cookiecutter git@github.com:StormyOrg/cookiecutter.git
	make env
	make install
