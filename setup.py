import os
import re
import sys

from setuptools import setup, find_packages


with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()


# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = re.sub(
        "<!--- long-description-skip-begin -->.*<!--- long-description-skip-end -->",
        "",
        readme_file.read(),
        flags=re.S | re.M,
    )


setup(
    name = "catan",
    version = "0.0.1",
    description="Python module for simulating a game of Catan.",
    long_description=README,
    url="https://github.com/catanistic/settlers_of_catan",
    license = "GNU General Public License v3.0",
    packages=find_packages(exclude=["test*"]),
    install_requires=REQUIREMENTS,
    author = "Igor Ryzhkov",
    author_email = "igor@ryzhkov.dev",
)