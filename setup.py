# -*- encoding: utf-8 -*-

import sys
from setuptools import setup

min_python = (3,5)
curr_python = sys.version_info

if curr_python < min_python:
    print("Tenko requires Python %d.%d or later" % min_python)
    sys.exit(1)

install_requires = []

with open('README.rst', 'r') as fd:
    long_description = fd.read()

setup(
    name='tenko',
    author='The Tenko Team (see AUTHORS file)',
    author_email='tenko@dynosoft.org',
    url='https://tenko.readthedocs.org/'
    description='Network abuse detection system',
    long_description=long_description,
    license='ISC',
    platforms=['Linux'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: ISC License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security',
    ],
    packages=['tenko'],
    entry_points={
        'console_scripts': [
            'tenko = tenko:main',
        ]
    },
    install_requires=install_requires,
)
