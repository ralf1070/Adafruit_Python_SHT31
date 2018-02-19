#!/usr/bin/env python
from os.path import join, dirname
from setuptools import setup
import sys
import os

f = open(join(dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()

setup(name = 'Adafruit_SHT31',
      version = '1.0.2',
      license = 'MIT',
      description = 'Python Library for Adafruit SHT31 module',
      long_description = long_description,
      url = 'https://github.com/ralf1070/Adafruit_Python_SHT31',
      py_modules = ['Adafruit_SHT31'],
      keywords = ['SHT31'],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
      ],
)
