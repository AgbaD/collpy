#!/usr/bin/python
# Author:   @BlankGodd_

from setuptools import setup

with open('description.rst', 'r') as fh:
    long_description = fh.read()

setup(
    name="collpy",
    version="0.0.4",
    author="Damilare Agbabiaka (BlankGodd)",
    author_email="blankgodd33@gmail.com",
    description="Add color highlights, load bars, progress displays and style to your python scripts and shell sessions",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/BlankGodd/collpy",
    py_modules=["collpy","base","fancy","progressbar"],
    package_dir = {"":"collpy"},
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Home Automation",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Terminals",
        "Topic :: Multimedia :: Graphics :: Presentation",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Fonts",
        "Typing :: Typed"
    ],  
    python_requires='>=3.6',
    project_urls={
        "Bug Reports": "https://github.com/BlankGodd/collpy/issues",
        "Read the Docs": "https://github.com/BlankGodd/collpy",
    },
    keywords=["progress", "loadbars", "highlight", "percentage", "style",
             "random", "ansi"],
)
