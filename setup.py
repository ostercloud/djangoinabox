# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import helloLNUP
version = helloLNUP.__version__

setup(
    name='helloLNUP',
    version=version,
    author='',
    author_email='allen.oster@rackspace.com',
    packages=[
        'helloLNUP',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['helloLNUP/manage.py'],
)