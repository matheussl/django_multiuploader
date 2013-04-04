#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-multiuploader-file",
    version = "2.0",
    author = "Matheus Lima",
    author_email = "matheus.se@gmail.com",
    description = ("A fork of django-multiuploader that allow upload any file type."),
    license = "Apache License 2.0",
    keywords = "django ios notification push",
    url = "https://github.com/matheussl/django_multiuploader",
    packages=['multiuploader',],
    long_description="N/A",

    requires = [
        'PIL',
        'sorl-thumbnail',
    ],
)