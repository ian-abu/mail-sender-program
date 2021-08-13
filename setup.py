from setuptools import setup, find_packages
import codecs
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION  = f.read()
    
VERSION = '1.4'
DESCRIPTION = 'gmail sending lib'
URL = 'https://pypi.org/project/mail-sending-program/'
# Setting up
setup(
    name="mail sending program",
    version=VERSION,
    author="py devoleper",
    author_email="<mail.program.help@gmail.com>",
    url=URL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'gmail', 'html', 'smtplib', 'auto', 'random'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta",
        "Operating System :: POSIX :: Linux",
    ],
    license='MIT'
)
