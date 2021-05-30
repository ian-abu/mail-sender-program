
from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'gmail sending lib'
LONG_DESCRIPTION = 'a library that sends gmail in 2 lines of code'

# Setting up
setup(
    name="mail sending program",
    version=VERSION,
    author="py devoleper",
    author_email="<mailsender.help@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'gmail', 'html', 'stmlp'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)