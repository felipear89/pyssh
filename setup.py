# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sytssh',
    version='0.0.1',
    description='A ssh helper to save your time',
    long_description=readme,
    author='Felipe Alexandre Rodrigues',
    author_email='felipear89@gmail.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    scripts = ['bin/sytssh'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
