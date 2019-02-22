#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installation script for `orion.algo.{{ cookiecutter.plugin_name }}`."""
import os

from setuptools import setup

import versioneer


repo_root = os.path.dirname(os.path.abspath(__file__))

tests_require = ['pytest>=3.0.0']

setup_args = dict(
    name='orion.algo.{{ cookiecutter.plugin_name }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='{{ cookiecutter.short_description }}',
    long_description=open(os.path.join(repo_root, "README.rst")).read(),
    license='BSD-3-Clause',
    author=u'{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{ cookiecutter.plugin_name }}',
    packages=['orion.algo.{{ cookiecutter.plugin_name }}'],
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'OptimizationAlgorithm': [
            '{{ cookiecutter.plugin_name }}_{{ cookiecutter.algo_name }} = orion.algo.{{ cookiecutter.plugin_name }}.{{cookiecutter.algo_name }}'
            ],
        },
    install_requires=['orion.core'],
    tests_require=tests_require,
    setup_requires=['setuptools', 'pytest-runner>=2.0,<3dev'],
    extras_require=dict(test=tests_require),
    # "Zipped eggs don't play nicely with namespace packaging"
    # from https://github.com/pypa/sample-namespace-packages
    zip_safe=False
    )

setup_args['keywords'] = [
    'Machine Learning',
    'Deep Learning',
    'Distributed',
    'Optimization',
    ]

setup_args['platforms'] = ['Linux']

setup_args['classifiers'] = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GPU GPLv3',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
] + [('Programming Language :: Python :: %s' % x)
     for x in '3 3.5 3.6 3.7'.split()]

if __name__ == '__main__':
    setup(**setup_args)
