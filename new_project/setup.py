#!/usr/bin/python3

from setuptools import setup, find_packages


NAME = 'CHANGE_THIS_NAME'


def get_requirements():
    with open('requirements.txt') as fd:
        content = fd.read().splitlines()
    return [line for line in content if not line.startswith('#')]


setup(
    name=NAME,
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='CHANGE_THIS_AUTHOR',
    author_email='CHANGE_THIS_AUTHOR_EMAIL@redhat.com',
    maintainer='CHANGE_THIS_AUTHOR',
    maintainer_email='CHANGE_THIS_EMAIL@redhat.com',
    keywords='fabric8-analytics openshiftio',
    url='https://github.com/fabric8-analytics/CHANGE_THIS_PROJECT_NAME',
    license='CHANGE_THIS_LICENSE',
    description='CHANGE_THIS_DESCRIPTION',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
    ]
)
