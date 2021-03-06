# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='b2',
    version=version,
    description='Command line client for B2 Cloud Storage',
    long_description=long_description,
    url='https://github.com/e12e/B2_Command_Line_Tool',
    author='Eirik Schwenke',
    author_email='github@s.hypertekst.net',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: System :: Archiving :: Backup',
        'Environment :: Console',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='cloud storage backup',

    py_modules=["b2"],
    install_requires=['docopt>=0.6.1'],

    data_files = [("", ["VERSION", "usage.txt"])],

    entry_points={
        'console_scripts': [
            'b2=b2:main',
        ],
    },
)
