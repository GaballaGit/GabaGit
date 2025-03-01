#!/usr/bin/env python3

from setuptools import setup

setup ( name = 'gabagit',
       version = '1.0',
       packages = ['gabagit'],
       entry_points = {
           'console_scripts' : [
               'gabagit = gabagit.cli:main'
               ]
           })


