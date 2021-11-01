# coding: utf-8
from setuptools import setup, find_packages

with open("README.md", "r" ,encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ConfigController",
    version="0.2.0",
    author="Fumiya-Shibamata",
    author_email="fumi_siba@yahoo.co.jp",
    description="easy control config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbfm/ConfigController",
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': ''},
    python_requires='>=3.6',
)
