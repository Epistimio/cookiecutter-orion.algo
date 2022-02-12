{%- from "macros/rst" import doc_title, doc_subtitle -%}

{{ doc_title('orion.algo.' + cookiecutter.plugin_name) }}


|pypi| |py_versions| |license| |codecov| |github-actions|


.. |pypi| image:: https://img.shields.io/pypi/v/orion.algo.{{cookiecutter.plugin_name}}
    :target: https://pypi.python.org/pypi/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Current PyPi Version

.. |py_versions| image:: https://img.shields.io/pypi/pyversions/orion.algo.{{cookiecutter.plugin_name}}.svg
    :target: https://pypi.python.org/pypi/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Supported Python Versions

.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause
    :alt: BSD 3-clause license

.. |codecov| image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}
    :alt: Codecov Report

.. |github-actions| image:: https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}/workflows/build/badge.svg?branch=master&event=pull_request
    :target: https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}/actions?query=workflow:build+branch:master+event:schedule
    :alt: Github actions tests



{{cookiecutter.short_description}}


----

This ``orion.algo`` plugin was generated with `Cookiecutter`_ along with `@Epistimio`_'s `cookiecutter-orion.algo`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install ``orion.algo.{{cookiecutter.plugin_name}}`` via pip

.. code-block:: console

    $ pip install git+https://github.com/{{ cookiecutter.github_username }}/orion.algo.{{cookiecutter.plugin_name}}.git


Contribute or Ask
-----------------

Do you have a question or issues? Do you want to report a bug or suggest a feature? Name it! Please
contact us by opening an issue in our repository below and checkout Oríon's
`contribution guidelines <https://github.com/Epistimio/orion/blob/develop/CONTRIBUTING.md>`_:

- Issue Tracker: `<https://github.com/{{cookiecutter.github_username}}/orion.algo.{{cookiecutter.plugin_name}}/issues>`_
- Source Code: `<https://github.com/{{cookiecutter.github_username}}/orion.algo.{{cookiecutter.plugin_name}}>`_

Start by starring and forking our Github repo!

Thanks for the support!

Citation
--------

If you use this wrapper for your publications, please cite both
`ADD WRAPPED LIBRARY's NAME HERE <URL TO CITATION SECTION OF THE WRAPPED LIBRARY>` and 
`Oríon <https://github.com/epistimio/orion#citation>`.

License
-------

Distributed under the terms of the BSD-3-Clause license,
``orion.algo.{{cookiecutter.plugin_name}}`` is free and open source software.


.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@Epistimio`: https://github.com/Epistimio
.. _`cookiecutter-orion.algo`: https://github.com/Epistimio/cookiecutter-orion.algo
.. _`file an issue`: https://github.com/{{cookiecutter.github_username}}/cookiecutter-orion.algo.{{cookiecutter.plugin_name}}/issues
.. _`orion`: https://github.com/Epistimio/orion
