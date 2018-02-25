# Copyright (c) 2018 Patrick Pedersen <ctx.xda@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = "Mkauthdocs is a tool specifically made to implement simple authentication around [mkdocs](www.mkdocs.com) builds."

setup(
    name='mkauthdocs',
    version='0.1.2',
    description='An authentication tool for mkdocs builds',
    long_description=long_description,
    url='https://github.com/ctxz/mkauthdocs',
    author='Patrick Pedersen',
    author_email='ctx.xda@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='mkdocs authentication documentation',

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'mkauthdocs=mkauthdocs.__main__:main',
        ],
    },

    project_urls={  # Optional
        'Mkdocs': 'http://www.mkdocs.org/',
        'Bug Reports': 'https://github.com/ctxz/mkauthdocs/issues',
        'Source': 'https://github.com/ctxz/mkauthdocs/',
    },
)
