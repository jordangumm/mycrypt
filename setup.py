#!/usr/bin/env python

from distutils.core import setup

setup(name='mycrypt',
      version='0.1',
      description='secure file and message management tool',
      author='Jordan Gumm',
      author_email='jngumm@gmail.com',
      license='MIT'
      packages=['mycrypt'],
      scripts=['bin/save-file-to-crypt', 'bin/recover-file-from-crypt'],
      install_requires=[
          'click',
          'pyaml',
          'simplecrypt',
      ],
)
