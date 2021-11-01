from setuptools import setup

setup()


# coding: utf-8
from setuptools import setup, find_packages

#with open("README.md", "r" ,encoding='utf-8') as fh:
#    long_description = fh.read()

setup(
    name="ConfigController",
    version="0.2.0",
    license='MIT License',
    description="easy control config",

    author="Fumiya-Shibamata",
    author_email="fumi_siba@yahoo.co.jp",
    url="https://github.com/sbfm/ConfigController",

    packages=find_packages('src'),
    package_dir={'': 'src'},
    #py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    #python_requires='>=3.6',
    #long_description=long_description,
    #long_description_content_type="text/markdown",
)
