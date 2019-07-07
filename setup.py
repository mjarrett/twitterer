#!/usr/bin/env python3

from distutils.core import setup

setup(name='Twitterer',
      version='1.0',
      description='Wrapper for Tweepy',
      author='Mike Jarrett',
      author_email='msjarrett@gmail.com',
      packages=['twitterer'],
      install_requires=[
          'tweepy',
      ]
     )
