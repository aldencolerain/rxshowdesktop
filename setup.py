# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


# package settings
setup(

    # info
    name='rxshowdesktop',
    version='0.0.1',
    author='Alden',
    url='https://github.com/aldencolerain/rxshowdesktop.git',
    description='Desktop toggle for for Xubuntu.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",

    # include
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,

    # public dependencies
    install_requires=[],

    # keep this package private
    classifiers=['Private :: Do Not Upload'],

    # cli scripts
    entry_points={'console_scripts': ['rxshowdesktop = rxshowdesktop.cli:main']},
)
