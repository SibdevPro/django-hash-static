#!/usr/bin/env python
import os
from setuptools import setup


long_description = open(os.path.join(os.path.dirname(__file__),
                                     'README.md')).read()


setup(
      name='django-hash-static',
      version='0.1',
      author='sibdev',
      author_email='a@sibdev.pro',

      packages=[
        'django_hash_static',
        'django_hash_static.templatetags',
      ],

      url='https://github.com/dmitry-morgachev/django-hash-static',
      license='BSD',
      description='Приложение с template tag, расширяющим возможности работы со статикой',
      long_description=long_description,

      platforms=['any'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
