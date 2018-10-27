#! /usr/bin/env python

from setuptools import setup

setup(
    name="dash-google-auth",
    version='0.1.0',
    description="Dash Google Auth",
    long_description=open('README.md', 'r').read().strip(),
    long_description_content_type='test/markdown',
    author="Lucas Chapin", author_email='lucas@altschool.com',
    url="https://github.com/lucaschapin/dash-google-auth",
    license=open('LICENSE', 'r').read().strip(),
    package='dash_google_auth',
    packages=['dash_google_auth'],
    install_requires=[
        'dash>=0.26.5',
        'dash-core-components>=0.28.3',
        'dash-html-components>=0.12.0',
        'Flask>=0.12.4',
        'Flask-Dance>=0.14.0',
        'six>=1.11.0',
    ],
    tests_require=['pytest'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
