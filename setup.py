# coding: utf-8
from setuptools import setup, find_packages
from glob import glob

#with open("README.md", "r" ,encoding='utf-8') as fh:
#    long_description = fh.read()

setup(
    name="ConfigController",
    version="0.2.0",
    license='MIT',
    description="easy control config",

    author="Fumiya-Shibamata",
    url="https://github.com/sbfm/ConfigController",

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    #python_requires='>=3.6',
    #long_description=long_description,
    #long_description_content_type="text/markdown",
)
