# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='black',
    version='23.3.0',
    description='The uncompromising code formatter.',
    author_email='Łukasz Langa <lukasz@langa.pl>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    install_requires=[
        'click>=8.0.0',
        'mypy-extensions>=0.4.3',
        'packaging>=22.0',
        'pathspec>=0.9.0',
        'platformdirs>=2',
        'tomli>=1.1.0; python_version < "3.11"',
        'typed-ast>=1.4.2; python_version < "3.8" and implementation_name == "cpython"',
        'typing-extensions>=3.10.0.0; python_version < "3.10"',
    ],
    extras_require={
        'colorama': [
            'colorama>=0.4.3',
        ],
        'd': [
            'aiohttp>=3.7.4',
        ],
        'jupyter': [
            'ipython>=7.8.0',
            'tokenize-rt>=3.2.0',
        ],
        'uvloop': [
            'uvloop>=0.15.2',
        ],
    },
    entry_points={
        'console_scripts': [
            'black = black:patched_main',
            'blackd = blackd:patched_main [d]',
        ],
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["_black_version"],
    package_data={
        "blib2to3": ["*.txt"],
        "black": ["py.typed"],
    },
)
