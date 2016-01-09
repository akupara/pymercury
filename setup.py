from distutils.core import setup

from setuptools import find_packages

setup(
        name='pymercury',
        version='1.0',
        packages=find_packages(),
        url='https://github.com/akupara/pymercury',
        license='MIT',
        author='Lei Sun',
        author_email='leix.sun@qq.com',
        description='Utilities for SQLAlchemy and Alembic',
        install_requires=[
            'SQLAlchemy>=1.0.8',
            'alembic>=0.8.3'
        ],
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
