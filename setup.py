"""Python setup.py for stage_build package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("stage_build", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="stage_build",
    version=read("stage_build", "VERSION"),
    description="Awesome stage_build created by hakehuang",
    url="https://github.com/hakehuang/stage_build/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="hakehuang",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["stage_build = stage_build.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
