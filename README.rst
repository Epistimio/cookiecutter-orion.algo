=========================
Orion Algorithm Template
=========================

 .. _travis: https://travis-ci.org/Epistimio/cookiecutter-orion.algo
 .. |travis.png| image:: https://travis-ci.org/Epistimio/cookiecutter-orion.algo.png
    :alt: Travis CI build status
    :target: `travis`_

|travis.png|

.. _Cookiecutter: http://cookiecutter.readthedocs.org
.. _Python Packaging User Guide: https://packaging.python.org/en/latest/distributing.html#configuring-your-project
.. _Packaging a Python library: http://blog.ionelmc.ro/2014/05/25/python-packaging


This is a `Cookiecutter`_ template for creating a Orion Algorithm Plugin.


Usage
=====

.. _GitHub: https://github.com/Epistimio/cookiecutter-orion.algo


Install Python requirements to use the template:

.. code-block:: console

    $ python -m pip install cookiecutter>=1.5 versioneer>=0.18 jinja2


Create a new project directly from the template on `GitHub`_:

.. code-block:: console
   
    $ cookiecutter gh:Epistimio/cookiecutter-orion.algo
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

+-----------------------+--------------------------------------------+--+
| Field                 | Description                                |  |
+-----------------------+--------------------------------------------+--+
| ``plugin_name``       | Will be used for orion.algo.plugin_name    |  |
+-----------------------+--------------------------------------------+--+
| ``author_name``       | For metadata of python package             |  |
+-----------------------+--------------------------------------------+--+
| ``author_short``      | For metadata of python package             |  |
+-----------------------+--------------------------------------------+--+
| ``author_email``      | For metadata of python package             |  |
+-----------------------+--------------------------------------------+--+
| ``github_username``   | Username to build the url for installation |  |
+-----------------------+--------------------------------------------+--+
| ``copyright``         | For the BSD-3 license                      |  |
|                       | (You can change the license)               |  |
+-----------------------+--------------------------------------------+--+
| ``short_description`` | For metadata of python package             |  |
+-----------------------+--------------------------------------------+--+
| ``synopsis``          | For documentation in algo module           |  |
+-----------------------+--------------------------------------------+--+
| ``algo_name``         | Name for the algorithm class               |  |
+-----------------------+--------------------------------------------+--+
| ``algo_module_name``  | Name of the algorihtm module               |  |
+-----------------------+--------------------------------------------+--+

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

.. code-block:: python

    def seed_rng(self, seed):

Explain main points. Algo must be copiable with get_state, set_state, seedable, etc.


.. code-block:: python

    @property
    def state_dict(self):

The state dict is used to copy algorithms within the parallel strategy. All algorithms must provide
a state dict to ensure that we reset it to a previous state.

.. code-block:: python

    def set_state(self, state_dict):

Stateful attributes of the algorithm are reset using the given ``state_dict``. Note that
``set_state`` must be compliant with ``state_dict`` and use
the same structure.

.. code-block:: python

    def suggest(self, num=1):

The method to suggest new trials. The argument ``num=1``
request the number of trials that the algorithm must sample. Note that it is possible to only
support ``num=1`` and raise ValueError otherwise.

.. code-block:: python

    def observe(self, points, results):

The method to observe results of suggested trials. Note that observe may be called several times for
the same points. Make sure to handle this properly within your algorithm if this is problematic.
Points are passed as a list of lists, each list representing the value of the params in the order
defined in ``self.space``


TODO Give explanation of what is passed in builder (space, seed, etc)
 also how does it work to define now arugmnets? That's confusing!

TODO: Give explanation for the attribute ``requires``.

Tests
=====

To test the freshly built package, you must first install the requirements. From within the new
package, run

.. code-block:: console

    $ pip install -r tests/requirements.txt

You can then run the unit-tests with 

.. code-block:: console

    $ pytest tests/integration_test.py

or using ``tox``

.. code-block:: console

    $ tox -e py36

Note that the algorithm pre-built is random search so that you can start from a fully working
environment and test your way through the modifications.

There is also the option of running the toy-benchmark to compare the performance of your algorithm
with random search and bayesian optimization. First install the requirements.

.. code-block:: console

    $ pip install -r tests/benchmark/requirements.txt

And then execute the benchmark

.. code-block:: console

    $ pytest tests/benchmark/main.py

or using ``tox``

.. code-block:: console

    $ tox -e benchmark

TODO Setup tox and travis in cookiecutter to test the pre-built tests

TODO 
1. Verify tox in cookiecutter
2. Confirm benchmark --no-xserver works
3. Verify tox in template
4. Try transfering command in cookiecutter-tox to template-tox (instead of pytest and python
   benchmark/main.py directly, use tox -e py36 and tox -e benchmark)
5. Push to repo and set Travis for cookiecutter

Contribute
==========

TODO
How do I get my algo moved into github.org/Epistimio to make it an official plugin?
