from setuptools import find_packages, setup

with open("requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="AGA8-Detail",
    description="A package to approximate the compressibility factor, z of a gas using P, T and gas composition, x.",
    version="1.0.0",
    author="Dan Seal",
    install_requires=requirements,
    packages=find_packages(),
)
