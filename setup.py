# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-tinkoff',
    version='0.41',
    author='Ivanov S',
    author_email='nameoff.nv@gmail.com',
    packages=['django_tinkoff_merchant'],
    url='https://github.com/django/django-tinkoff',
    license='MIT',
    description='Tinkoff merchant integration',
    install_requires=['django>=1.8.0', 'requests>=2.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ]
)