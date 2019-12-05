=========================
Orion Algorithm Template
=========================

 .. _travis: https://travis-ci.org/bouthilx/cookiecutter-orion.algo
 .. |travis.png| image:: https://travis-ci.org/bouthilx/cookiecutter-orion.algo.png
    :alt: Travis CI build status
    :target: `travis`_

|travis.png|

.. _Cookiecutter: http://cookiecutter.readthedocs.org
.. _Python Packaging User Guide: https://packaging.python.org/en/latest/distributing.html#configuring-your-project
.. _Packaging a Python library: http://blog.ionelmc.ro/2014/05/25/python-packaging


This is a `Cookiecutter`_ template for creating a Orion Algorithm Plugin.


Usage
=====

.. _GitHub: https://github.com/bouthilx/cookiecutter-orion.algo


Install Python requirements to use the template:

.. code-block:: console

    $ python -m pip install cookiecutter>=1.5 versioneer>=0.18 jinja2


Create a new project directly from the template on `GitHub`_:

.. code-block:: console
   
    $ cookiecutter gh:bouthilx/cookiecutter-orion.algo
    plugin_name []: skopt
    author_name []: Xavier Bouthillier
    author_short [Author Name]:
    author_email []: xavier.bouthillier@umontreal.ca
    github_username []: bouthilx
    copyright [2019, Author Name]:
    short_description [TODO]:
    synopsis [TODO]:
    algo_name []: BayesianOptimizer
    algo_module_name [bayesianoptimizer]: bayes

+-----------------------+-----------------------------------------+
| Field                 | Description                             |
+-----------------------+-----------------------------------------+
| ``plugin_name``       | Will be used for orion.algo.plugin_name |
+-----------------------+-----------------------------------------+
| ``author_name``       | For metadata of python package          |
+-----------------------+-----------------------------------------+
| ``author_short``      | For metadata of python package          |
+-----------------------+-----------------------------------------+
| ``author_email``      | For metadata of python package          |
+-----------------------+-----------------------------------------+
| ``github_username``   | bouthilx                                |
+-----------------------+-----------------------------------------+
| ``copyright``         | For the BSD-3 license                   |
|                       | (You can change the license)            |
+-----------------------+-----------------------------------------+
| ``short_description`` | For metadata of python package          |
+-----------------------+-----------------------------------------+
| ``synopsis``          | For documentation in algo module        |
+-----------------------+-----------------------------------------+
| ``algo_name``         | Name for the algorithm class            |
+-----------------------+-----------------------------------------+
| ``algo_module_name``  | Name of the algorihtm module            |
+-----------------------+-----------------------------------------+

This will create package structure. 

::

    orion.algo.{plugin_name}
    ├── README.rst
    ├── setup.cfg
    ├── setup.py
    ├── MANIFEST.in
    ├── LICENSE (BSD License)
    ├── versioneer.py 
    ├── tox.ini
    ├── doc
    │   ├── requirements.txt
    │   └── src
    │       ├── conf.py
    │       └── index.rst
    ├── tests
    │   ├── requirements.txt
    │   └── benchmark
    │       ├── requirements.txt
    │       ├── main.py
    │       ├── rosenbrock.py
    │       ├── {algoname}.yaml
    │       ├── bayesopt.yaml
    │       └── random_search.yaml
    └── src
        └── orion
            └── algo
                └── {plugin_name}
                    ├── {algoname}.py
                    └── _version.py

``LICENSE``

    (Note that you are free to change the License, copyright is to your name)

``versioneer.py``
``src/orion/algo/{plugin_name}/_version.py``

   (to version automatically your algo, just ignore these if you don't plan to make releases)

``tests``

   Automatically generated tests

``tests/benchmark``

   Automatically generated benchmark test using the yaml files
   created in the same folder.

``doc``

   Automatically generated template for documentation

``tox.ini``

   Tox file defining commands to run tests, build doc and publish code.


The important files to modify are ``src/orion/algo/{plugin_name}/{module_name}.py`` to implement the
algorithm and ``tests/benchmark/{algo_name}.yaml`` to fill the arguments required for the algorithm
you implement.


Implementation
==============

Explain what to do.

Explain main points. Algo must be copiable with get_state, set_state, seedable, etc.


Tests
=====

How do we test?


Contribute
==========

How do I get my algo moved into github.org/Epistimio to make it an official plugin?
