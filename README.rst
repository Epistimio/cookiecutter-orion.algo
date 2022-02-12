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

    $ pip install -r requirements.txt


Create a new project directly from the template on `GitHub`_:

.. code-block:: console
   
    $ cookiecutter gh:Epistimio/cookiecutter-orion.algo
    plugin_name []: skopt
    author_name []: Xavier Bouthillier
    author_short [Author Name]:
    author_email []: xavier.bouthillier@umontreal.ca
    github_username []: bouthilx
    copyright [2021, Author Name]:
    short_description [TODO]:
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
| ``algo_name``         | Name for the algorithm class               |  |
+-----------------------+--------------------------------------------+--+
| ``algo_module_name``  | Name of the algorihtm module               |  |
+-----------------------+--------------------------------------------+--+

This will create the following package structure.

::

    orion.algo.{plugin_name}
    ├── README.rst
    ├── setup.cfg
    ├── setup.py
    ├── MANIFEST.in
    ├── LICENSE (BSD License)
    ├── versioneer.py 
    ├── tox.ini
    ├── dev-requirements.txt
    ├── doc
    │   ├── requirements.txt
    │   └── src
    │       ├── conf.py
    │       └── index.rst
    ├── tests
    │   ├── requirements.txt
    │   ├── integration_test.py
    │   └── benchmark.py
    └── src
        └── orion
            └── algo
                └── {plugin_name}
                    ├── {algoname}.py
                    ├── __init__.py
                    └── _version.py

The important files to modify are ``src/orion/algo/{plugin_name}/{module_name}.py`` to implement the
algorithm and ``tests/benchmark/{algo_name}.yaml`` to fill the arguments required for the algorithm
you implement.

``LICENSE``

Note that you are free to change the License, copyright is to your name.

``versioneer.py``
``src/orion/algo/{plugin_name}/_version.py``

This serves to version automatically your algo, just ignore these if you don't plan to make releases.

``tests``

These are the automatically generated tests.

``tests/benchmark``

Automatically generated benchmark test using the yaml files created in the same folder.

``doc``

Automatically generated template for documentation

``tox.ini``

Tox file defining commands to run tests, build doc and publish code.

Implementation
==============


+-----------------------------------------------------------------------------------+
| Tip                                                                               |
+-----------------------------------------------------------------------------------+
| The cookiecutter creates a fully functionning random search plugin.               |
| All tests should pass right away. Make sure your environment is setup properly    |
| and that all tests are passing as expected before making any changes in the code. |
+-----------------------------------------------------------------------------------+

Base attributes & methods
-------------------------

.. code-block:: python

    class YourAlgorithm(BaseAlgorithm):
        requires_type = "real"
        requires_dist = "linear"
        requires_shape = "flattened"

Some algorithms have special requirements on the data. Maybe the search space should be real only,
logarithmic distributions should be linearized, or multidimensional
data should be flattened. The algorithm class can specify
these special requirements through the class attributes
``requires_type``, ``requires_dist`` and ``requires_shape``. 
See documentation of `build_required_space`_ to see the special
requirements supported.

When Oríon will instantiate an algorithm, it will wrap it
in a `SpaceTransformAlgoWrapper`_ and create a transformed space 
based on the requirements. The ``SpaceTransformAlgoWrapper`` will
take care of converting the hyperparameters so that they are
compliant with the search space outsite the algorithm and
compliant with the algorithm's requirements when passed to the algorithm.

Suppose the algorithm has ``requires_type = "real"``, then
Oríon will assign a transformed space to the algorithm in which
all dimensions are transformed to be real. For instance, categorical dimensions are turned to
one-hot vectors. The algorithm can then work in this real space
solely. When the algorithm suggest trials, the 
`SpaceTransformAlgoWrapper`_ will convert the hyperparameters
of these trials so that they are valid in the original space. For
instance, one-hot vectors are converted back to categorical values.

.. code-block:: python

    @property
    def space(self):
        """Domain of problem associated with this algorithm's instance."""
        return self._space

    @space.setter
    def space(self, space):
        """Set space."""
        self._space = space

At creation time, the algorithm is passed the original space
as argument ``space`` to its constructor ``__init__``.
The algorithm is then assigned the transformed space through the setter
``algorithm.space = transformed_space``.
This is the right place to keep a reference to the original space if you need to.
See `skopt's implementation`_ for an example. Keeping a reference to the original space
can be useful for instance to verify if an algorithm has tried every possible values
in the original space. See ``is_done()`` implementation of `skopt's implementation`_ for
an example using the original space.

.. _skopt's implementation: https://github.com/Epistimio/orion.algo.skopt/blob/master/src/orion/algo/skopt/bayes.py


+--------------------------------------+-----------------------------------------------------------+
| Tests that should pass at this point | Description                                               |
+--------------------------------------+-----------------------------------------------------------+
| ``test_get_id``                      | Test that id of trial is computed properly.               |
+--------------------------------------+-----------------------------------------------------------+
| ``test_configuration``               | Test that configuration contains all expected attributes. |
+--------------------------------------+-----------------------------------------------------------+


.. _build_required_space: https://orion.readthedocs.io/en/stable/code/core/worker/transformer.html#orion.core.worker.transformer.build_required_space

.. _SpaceTransformAlgoWrapper: https://orion.readthedocs.io/en/stable/code/core/worker/primary_algo.html#orion.core.worker.primary_algo.SpaceTransformAlgoWrapper

.. code-block:: python

    def __init__(self, space, seed=None, some='other', custom='arguments'):
        super(YourAlgorithm, self).__init__(space, seed=seed, some=some, custom=custom)


The initialization of the algorithm must pass space and seed to ``super().__init__``, but must also
pass any other argument that should be part of the configuration of the algorithm. Any argument passed
to ``super()`` will be assigned as an attribute to the algorithm and will be included in
``algo.configuration``, which is used to save the configuration of the algorithm in storage.


.. code-block:: python

    def suggest(self, num):

The method to suggest new trials. The argument ``num``
request the number of trials that the algorithm must sample. The algorithm may return less
than ``num`` if it is impossible to return more, and even return an empty list when
it is not possible to suggest a new trial. This may happen for example if there are too many trials
still being executed.

The algorithm should verify with ``self.has_suggested(trial)`` if a trial
was already suggested to make sure trials returned by ``suggest()`` are new ones.
Before returning a new trial, make sure to register it with ``self.register(trial)``
so that ``self.has_suggested(trial)`` works properly.

+----------------------------------------------------------------------------------------------+
| Tip                                                                                          |
+----------------------------------------------------------------------------------------------+
| Utility functions in `format_trials`_ are convenient to convert sets of hyperparameters from |
| dictionary format or list of values to ``Trial`` objects.                                    |
+----------------------------------------------------------------------------------------------+

.. _format_trials: https://orion.readthedocs.io/en/stable/code/core/utils/format_trials.html

+--------------------------------------+------------------------------------------------------+
| Tests that should pass at this point | Description                                          |
+--------------------------------------+------------------------------------------------------+
| ``test_suggest_n``                   | Test that the algorithm is able to suggest n trials. |
+--------------------------------------+------------------------------------------------------+
| ``test_has_suggested``               | Test that trials suggested are properly registered   |
+--------------------------------------+------------------------------------------------------+
| ``test_n_suggested``                 | Test that trials suggested are properly registered   |
|                                      | and counted.                                         |
+--------------------------------------+------------------------------------------------------+


.. code-block:: python

    def observe(self, trials):

The method to observe new status or results of trials. 
Observe may be called multiple time for the same trials until they are completed or broken.
See `Trial`_'s documentation for more information on their status or results attributes.
An observed trial should be registered using ``self.register(trial)`` so that
``self.has_observed(trial)`` can work properly. Note that ``has_observed(trial)`` may return
true only if a trial is completed. It will return False if a trial is broken.

All trials registered with ``self.register(trial)`` are stored in a dictionary 
``self._trials_info`` in the format 
``{self.get_id(trial): (trial, trial.objective.value if trial.objective else None)}``.


+------------------------------------------------------------------------------------------------+
| Warning                                                                                        |
+------------------------------------------------------------------------------------------------+
|   You should use ``self.get_id(trial)`` to get the trials ID in the original space.            |
|                                                                                                |
|   The ID of a trial may be different in a transformed space than in the original space.        |
|   This is because the ID is a hash of the trial's hyperparameters, and thus the transformation |
|   of the hyperparameters is affecting the hash. Only the ID in the original space matters      |
|   for Oríon and should be used to detect whether two trials are equal or equivalent in the     |
|   original search space.                                                                       |
+------------------------------------------------------------------------------------------------+


.. _Trial: https://orion.readthedocs.io/en/stable/code/core/worker/trial.html#orion.core.worker.trial.Trial

+--------------------------------------+--------------------------------------------------------+
| Tests that should pass at this point | Description                                            |
+--------------------------------------+--------------------------------------------------------+
| ``test_observe``                     | Test that algorithm can observe without any expection. |
|                                      | The validity of observe is not verified here.          |
+--------------------------------------+--------------------------------------------------------+
| ``test_has_observed``                | Test that observed completed trials are registered     |
|                                      | properly.                                              |
+--------------------------------------+--------------------------------------------------------+
| ``test_n_observed``                  | Test that observed completed trials are registered     |
|                                      | and counted properly.                                  |
+--------------------------------------+--------------------------------------------------------+
| ``test_real_data``                   | Test that algorithm can work with float values.        |
+--------------------------------------+--------------------------------------------------------+
| ``test_int_data``                    | Test that algorithm can suggest and observe            |
|                                      | discrete values                                        |
+--------------------------------------+--------------------------------------------------------+
| ``test_cat_data``                    | Test that algorithm can suggest and observe            |
|                                      | categorical values                                     |
+--------------------------------------+--------------------------------------------------------+
| ``test_logint_data``                 | Test that algorithm can work with discrete loguniform  |
|                                      | dimensions.                                            |
+--------------------------------------+--------------------------------------------------------+
| ``test_logreal_data``                | Test that algorithm can work with real loguniform      |
|                                      | dimensions.                                            |
+--------------------------------------+--------------------------------------------------------+
| ``test_shape_data``                  | Test that algorithm can work with arrays.              |
+--------------------------------------+--------------------------------------------------------+


.. code-block:: python

    def seed_rng(self, seed=None):

This method must seed the internal state of the algorithm so that it would always sample the same
sequence of points.

You may need to seed global random number generators such as ``random`` or ``numpy.random`` if you
are wrapping a third party library using them.

+--------------------------------------+---------------------------------------------------------+
| Tests that should pass at this point | Description                                             |
+--------------------------------------+---------------------------------------------------------+
| ``test_seed_rng``                    | Test that seeding the algorithm can be seeded properly. |
+--------------------------------------+---------------------------------------------------------+
| ``test_seed_rng_init``               | Test that the algorithm is seeded during instantiation. |
+--------------------------------------+---------------------------------------------------------+

.. code-block:: python

    @property
    def state_dict(self):

The state dict is used to store the algorithm's state in storage so that it can
be shared across runners (the main processes running the optimization).
Make sure to include any attribute that may change during the execution of the algorithm,
including the state of random number generator used. Return copies of these attributes
to avoid any side-effects.
There is no need to include the values of the algorithm's configuration.

.. code-block:: python

    def set_state(self, state_dict):

Stateful attributes of the algorithm are reset using the given ``state_dict``. Note that
``set_state`` must be compliant with ``state_dict`` and use
the same structure.

+--------------------------------------+------------------------------------------------------+
| Tests that should pass at this point | Description                                          |
+--------------------------------------+------------------------------------------------------+
| ``test_state_dict``                  | Test that state_dict can be used to resume algorithm |
|                                      | and sample the same trials deterministically.        |
+--------------------------------------+------------------------------------------------------+
| ``test_has_observed_statedict``      | Test that state_dict sets back observed trials.      |
+--------------------------------------+------------------------------------------------------+
| ``test_has_suggested_statedict``     | Test that state_dict sets back suggested trials.     |
+--------------------------------------+------------------------------------------------------+


.. code-block:: python

    def is_done(self, points, results):

This method is used to signal whether the algorithm is done or not. The base implementation
verifies if all possible values have been tried or whether more than ``self.max_trials`` trials
have been tried. ``self.max_trials`` is an attribute set by Oríon based on the experiments
``max_trials`` value, you should not add it to your algorithm's configuration.

You will need to overwrite this method if your algorithm use a transformed space, because
transformed space can have a larger domain than the original one 
(ex: working with real values instead integers). The original space is the one that matters
for the experiment and it should thus be the space used to infer whether all possible values
have been tried. See `skopt's implementation`_ for an example of a custom ``is_done``
implementation to handle transformed space.

+--------------------------------------+-------------------------------------------------------+
| Tests that should pass at this point | Description                                           |
+--------------------------------------+-------------------------------------------------------+
| ``test_is_done_cardinality``         | Test that algorithms is done when all possible values |
|                                      | has been tried.                                       |
+--------------------------------------+-------------------------------------------------------+
| ``test_is_done_max_trials``          | Test that algorithm is done when maximum number of    |
|                                      | trials have been tried.                               |
+--------------------------------------+-------------------------------------------------------+
| ``test_optimize_branin``             | Test that algorithm reaches a reasonable objective    |
|                                      | when optimizing branin.                               |
+--------------------------------------+-------------------------------------------------------+

Useful attributes & methods
---------------------------

The base algorithm class implements several other methods that rarely requires to be overwritten
but can prove very useful. Among 
In particular, you should pay attention to `get_id(trial)`_, `fidelity_index`_, `register(trial)`_,
`has_suggested(trial)`_, and `has_observed(trial)`_.

.. _get_id(trial): https://orion.readthedocs.io/en/stable/code/algo/base.html#orion.algo.base.BaseAlgorithm.get_id

.. _fidelity_index: https://orion.readthedocs.io/en/stable/code/algo/base.html#orion.algo.base.BaseAlgorithm.fidelity_index

.. _register(trial): https://orion.readthedocs.io/en/stable/code/algo/base.html#orion.algo.base.BaseAlgorithm.register

.. _has_suggested(trial): https://orion.readthedocs.io/en/stable/code/algo/base.html#orion.algo.base.BaseAlgorithm.has_suggested

.. _has_observed(trial): https://orion.readthedocs.io/en/stable/code/algo/base.html#orion.algo.base.BaseAlgorithm.has_observed

Tests
=====

To test the freshly built package, you must first install the requirements. From within the new
package, run

.. code-block:: console

    $ pip install -r dev-requirements.txt
    $ pip install -r tests/requirements.txt

You can then run the unit-tests with 

.. code-block:: console

    $ pytest tests/integration_test.py

or using ``tox``,

.. code-block:: console

    $ tox -e py36

Note that the algorithm pre-built is random search so that you can start from a fully working
environment and test your way through the modifications.

There is also the option of running the toy-benchmark to compare the performance of your algorithm
with random search and TPE.

.. code-block:: console

    $ python tests/benchmark.py

The benchmark will generate interactive plotly figures saved as ``Branin_AverageResult.html``
and ``RosenBrock_AverageResult.html``. 


Finally, official plugins must follow the same code quality standards than ``orion.core``. Therefore
there are tests included in the pre-built package for ``black``, ``isort`` and ``pylint``. You can
execute them with

.. code-block:: console

    $ tox -e black

To fix ``black`` or ``isort`` issues, you can use the tox commands ``run-black`` or ``run-isort``.
For example:

.. code-block:: console

    $ tox -e run-black
