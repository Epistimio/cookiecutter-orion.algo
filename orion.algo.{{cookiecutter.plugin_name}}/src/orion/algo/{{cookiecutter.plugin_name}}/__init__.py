# -*- coding: utf-8 -*-
"""
:mod:`orion.algo.{{ cookiecutter.plugin_name }} -- {{ cookiecutter.short_description }}
======================{{ '=' * cookiecutter.plugin_name|length }}===={{ '=' * cookiecutter.short_description|length }}

.. module:: {{ cookiecutter.plugin_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
from ._version import get_versions
from .registrar import {{ cookiecutter.registrardb_classname }}

VERSIONS = get_versions()
del get_versions

__descr__ = '{{ cookiecutter.short_description }}'
__version__ = VERSIONS['version']
__license__ = 'BSD 3-Clause'
__author__ = u'{{ cookiecutter.author_name }}'
__author_short__ = u'{{ cookiecutter.author_short }}'
__author_email__ = '{{ cookiecutter.author_email }}'
__copyright__ = u'{{ cookiecutter.copyright }}'
__url__ = 'https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{ cookiecutter.plugin_name }}'
