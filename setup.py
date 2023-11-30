import os

from setuptools import setup

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="adilo_api_client",
    description="Python package for Adilo",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Joshua Lim",
    url="https://github.com/JoshuaLim995/adilo-api-client",
    project_urls={
        "Issues": "https://github.com/JoshuaLim995/adilo-api-client/issues",
        "CI": "https://github.com/JoshuaLim995/adilo-api-client/actions",
        "Changelog": "https://github.com/JoshuaLim995/adilo-api-client/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["adilo_api_client"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
