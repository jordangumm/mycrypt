#!/usr/bin/env python

from setuptools import setup, find_packages

exclude = ['mycrypt.bin',]

setup(name='mycrypt',
      version='0.1',
      description='secure file and message management tool',
      author='Jordan Gumm',
      author_email='jngumm@gmail.com',
      license='MIT',
      packages=find_packages(exclude=exclude),
      include_package_data=True,
      scripts=['bin/place-file-in-crypt', 'bin/recover-file-from-crypt'],
      install_requires=[
          'click',
          'pyaml',
          'simple-crypt',
      ],
      zip_safe=True,
)
