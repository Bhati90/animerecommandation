from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="animep",
    version="0.1",
    author="kishan",
    packages=find_packages(),
    install_requires = requirements,
)