from subprocess import call

call(["git", "init"])
call(["git", "add", "*"])
call(["git", "commit", "-m", "Initial commit"])
call(["git", "remote", "add", "origin", "{{ cookiecutter.git_url }}"])
