from setuptools import setup, find_packages

setup(
    name="firstt-pypi_math_demo",
    version="0.1.0",
    package_dir={"":"src"},
    url="https://github.com/Vadim077/lagerev_fossdev",
    package_dir={"": "tdd/src"},
    packages=find_packages(where="src")
)
