# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in custom_laboratory/__init__.py
from custom_laboratory import __version__ as version

setup(
	name='custom_laboratory',
	version=version,
	description='Customisation to fit the need of small laboratory store',
	author='Duk Panhavad',
	author_email='panhavadd@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
