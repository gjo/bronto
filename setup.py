#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import find_packages, setup


description = 'OpenSocial implementation in pyramid'
here = os.path.abspath(os.path.dirname(__file__))
try:
    readme = open(os.path.join(here, 'README.rst')).read()
    changes = open(os.path.join(here, 'CHANGES.txt')).read()
    long_description = '\n\n'.join([readme, changes])
except:
    long_description = description


install_requires = [
    'colander',
    'pyramid',
    'pyramid_rpc',
    'pyramid_services',
    'pyramid_tm',
    'sqlalchemy',
    'zope.interface',
    'zope.sqlalchemy',
]
develop_require =[
    'pyramid_debugtoolbar',
    'waitress',
]
tests_require = [
    'webtest',
]


setup(
    name='bronto',
    version='0.1.dev0',
    description=description,
    long_description=long_description,
    author='OCHIAI, Gouji',
    author_email='gjo.ext@gmail.com',
    url='https://github.com/gjo/bronto',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    test_suite='bronto',
    tests_require=tests_require,
    extras_require={
        'develop': develop_require,
        'testing': tests_require,
    },
    entry_points={
        'paste.app_factory': ['main = bronto:app_factory'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Pyramid',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
