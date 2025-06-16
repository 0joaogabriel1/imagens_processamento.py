# setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imagens_processamento.py",
    version="0.0.1",
    author="Joao Gabriel Oliveira Carvalho",
    author_email="jotagesurf@gmail.com",
    description="Um pacote simples para processamento de imagens.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0joaogabriel1/imagens_processamento.py",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)