from setuptools import setup

setup(
    name='black',
    version='26.5.1',
    description='The uncompromising code formatter.',
    author_email='Łukasz Langa <lukasz@langa.pl>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    install_requires=[
        'click>=8.0.0',
        'mypy-extensions>=0.4.3',
        'packaging>=22.0',
        'pathspec>=1.0.0',
        'platformdirs>=2',
        'pytokens~=0.4.0',
        'tomli>=1.1.0; python_version < "3.11"',
        'typing-extensions>=4.0.1; python_version < "3.11"',
    ],
    extras_require={
        'colorama': [
            'colorama>=0.4.3',
        ],
        'd': [
            'aiohttp>=3.10',
        ],
        'jupyter': [
            'ipython>=7.8.0',
            'tokenize-rt>=3.2.0',
        ],
        'uvloop': [
            'uvloop>=0.15.2; sys_platform != "win32"',
            'winloop>=0.5.0; sys_platform == "win32"',
        ],
    },
    entry_points={
        'console_scripts': [
            'black = black:patched_main',
            'blackd = blackd:patched_main [d]',
        ],
        'validate_pyproject.tool_schema': [
            'black = black.schema:get_schema',
        ],
    },
    packages=[
        'black',
        'black.resources',
        'blackd',
        'blib2to3',
        'blib2to3.pgen2',
    ],
    package_dir={'': 'src'},
    py_modules=['_black_version'],
    package_data={
        'blib2to3': ['*.txt'],
        'black': ['py.typed'],
    },
)
