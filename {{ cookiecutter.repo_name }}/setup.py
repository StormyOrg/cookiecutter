from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="{{ cookiecutter.repo_name }}",
    packages=find_packages(),
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.project }}",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "pandas>=1.2.0",
    ],
    extras_require={
        "dev": [
            "pre-commit>=2.15.0",
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "bumpver>=2021.1113",
            "flask>=1.1.4<2.0",
            "black==21.9b0",
            "flake8==3.9.2",
            "mypy==0.910",
            "types-requests>=2.25.8",
        ],
    },
    python_requires=">=3.8",
)
