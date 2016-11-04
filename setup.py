#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess

setup(name="stitchclient",
      version="0.4.0",
      description="A Stitch API client for Python",
      author="Stitch",
      url="https://github.com/stitchdata/python-stitch-client",
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      packages=find_packages(),
      install_requires=["python-dateutil", "msgpack-python"])
