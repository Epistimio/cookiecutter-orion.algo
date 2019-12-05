{%- from "macros/rst" import doc_title, doc_subtitle -%}

{{ doc_title('orion.algo.' + cookiecutter.plugin_name) }}


.. |pypi| image:: https://img.shields.io/pypi/v/orion.algo.{{cookiecutter.plugin_name}}
    :target: https://pypi.python.org/pypi/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Current PyPi Version

.. |py_versions| image:: https://img.shields.io/pypi/pyversions/orion.algo.{{cookiecutter.plugin_name}}.svg
    :target: https://pypi.python.org/pypi/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Supported Python Versions

.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause
    :alt: BSD 3-clause license

.. |rtfd| image:: https://readthedocs.org/projects/orion.algo.{{cookiecutter.plugin_name}}/badge/?version=latest
    :target: https://orion.algo-{{cookiecutter.plugin_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Codecov Report

.. |travis| image:: https://travis-ci.org/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Travis tests


{{cookiecutter.short_description}}


----

This `orion.algo`_ plugin was generated with `Cookiecutter`_ along with `@Epistimio`_'s `cookiecutter-orion.algo`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "orion.algo.{{cookiecutter.plugin_name}}" via `pip`_ from `PyPI`_::

    $ pip install git+https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}.git


Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the BSD-3-Clause license,
"orion.algo.{{cookiecutter.plugin_name}}" is free and open source software.


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@Epistimio`: https://github.com/Epistimio
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`cookiecutter-orion.algo`: https://github.com/Epistimio/cookiecutter-orion.algo
.. _`file an issue`: https://github.com/{{cookiecutter.github_username}}/cookiecutter-orion.algo.{{cookiecutter.plugin_name}}/issues
.. _`orion`: https://github.com/Epistimio/orion
