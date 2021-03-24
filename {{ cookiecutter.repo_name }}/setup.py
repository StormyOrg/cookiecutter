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
            "pre-commit>=2.9.3",
            "pytest>=6.2.1",
            "pytest-cov>=2.10.1",
            "bumpver>=2021.1109",
            "black>=20.8b1",
            "mypy>=0.812",
            "flake8>=3.9.0"
        ],
    },
    python_requires=">=3.8",
)
