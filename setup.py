from distutils.core import setup

import os
import re
from setuptools import find_packages

READMEFILE = "README.md"
VERSIONFILE = os.path.join("pymercury", "__init__.py")
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"


def get_version():
    verstrline = open(VERSIONFILE, "rt").read()
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError(
                "Unable to find version string in %s." % VERSIONFILE)


setup(
        name='pymercury',
        version=get_version(),
        packages=find_packages(),
        url='https://github.com/akupara/pymercury',
        license='MIT',
        author='Lei Sun',
        author_email='leix.sun@qq.com',
        description='Utilities for SQLAlchemy and Alembic',
        install_requires=[
            'SQLAlchemy>=1.0.8',
            'alembic>=0.8.3',
            'unicodecsv>=0.14.1'
        ],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Natural Language :: English',
        ]
)
