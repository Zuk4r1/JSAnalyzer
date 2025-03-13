#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='JSAnalyzer',
    version='1.0',
    packages=find_packages(),
    description="",
    long_description=open('README.md').read(),
    author='Zuk4r1',
    url='https://github.com/Zuk4r1',
    install_requires=[
        'safeurl',
        'tornado',
        'jsbeautifier',
        'netaddr',
        'pycurl',
        'beautifulsoup4',  # Corregido: "BeautifulSoup4" -> "beautifulsoup4"
        'future'  # Agregado para compatibilidad con __future__
    ],
)
