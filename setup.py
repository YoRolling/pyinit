# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="pyinit",
    version="1.0.0",
    description="a command line tool to help you build python packages",
    license="MIT",
    author="YoRolling",
    author_email="walldr2161ly@163.com",
    url='https://github.com/YoRolling/pyinit',
    packages=find_packages(),
    install_requires=[
        'Click',
        'whaaaaat'
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points="""
        [console_scripts]
        pyinit=pyinit.index:cli
    """,
    project_urls={
        'Bug Reports': 'https://github.com/YoRolling/pyinit/issues',
        'Source': 'https://github.com/YoRolling/pyinit/'
    },
    package_data={  # Optional
        'sample': ['pyinit/templates/*'],
    },
    include_package_data=True
)
