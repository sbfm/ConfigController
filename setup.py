import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ConfigController",
    version="0.2.0",
    author="Fumiya-Shibaata",
    author_email="fumi_siba@yahoo.co.jp",
    description="easy control config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbfm/ConfigController",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
