# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="{{name}}",
    version="{{version}}",
    description="A pip package",
    license="{{license}}",
    author="{{author}}",
    packages=find_packages(),
    install_requires=[
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points="""
    """
)
