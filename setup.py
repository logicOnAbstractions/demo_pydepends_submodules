import pathlib
import setuptools


# This call to setup() does all the work
setuptools.setup(
    name="parentdir",
    version="0.0.1",
    description="A simple Python parent project that has a submodule with dependancies",
    long_description="a much longer description flasj flksaj df;lkaj sdl;kfj a;lsdjf alksdj flkajs dlfkj aslkdfj alksdf lasjd f asldfj laksjd flkja",
    long_description_content_type="text/x-rst",
    url="https://github.com/shunsvineyard/myproj",
    author="Author Name",
    author_email="author@email.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)