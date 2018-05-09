# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="pyinit",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="YoRolling",
    packages=find_packages(),
    install_requires=[
        'Click'
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points="""
        [console_scripts]
        pyinit=pyinit.index:cli
    """
)
