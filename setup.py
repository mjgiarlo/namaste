# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'namaste',
    version = '0.3.1',
    description = "a tool for working with Namaste directory description tags",
    author = "Michael J. Giarlo",
    author_email = "leftwing@alumni.rutgers.edu",
    url = "http://github.com/mjgiarlo/namaste",
    py_modules = ['namaste', 'ez_setup'],
    test_suite = 'test',
    scripts = ['bin/namaste']
)
