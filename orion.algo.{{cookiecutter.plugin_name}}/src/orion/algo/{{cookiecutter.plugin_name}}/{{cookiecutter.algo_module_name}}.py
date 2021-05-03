# -*- coding: utf-8 -*-
"""
:mod:`orion.algo.{{ cookiecutter.plugin_name }}.{{ cookiecutter.algo_module_name }} -- TODO
======================{{ '=' * cookiecutter.plugin_name|length }}==================

.. module:: {{ cookiecutter.algo_module_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
import numpy

from orion.algo.base import BaseAlgorithm


class {{ cookiecutter.algo_name }}(BaseAlgorithm):
    """TODO: Class docstring"""

    requires_type = None
    requires_dist = None
    requires_shape = None

    def __init__(self, space, seed=None):
        super({{ cookiecutter.algo_name }}, self).__init__(space, seed=seed)

    def seed_rng(self, seed):
        """Seed the state of the random number generator.

        :param seed: Integer seed for the random number generator.

        .. note:: This methods does nothing if the algorithm is deterministic.
        """
        # TODO: Adapt this to your algo
        self.rng = numpy.random.RandomState(seed)

    @property
    def state_dict(self):
        """Return a state dict that can be used to reset the state of the algorithm."""
        # TODO: Adapt this to your algo
        return {'rng_state': self.rng.get_state(), "_trials_info": copy.deepcopy(self._trials_info)}

    def set_state(self, state_dict):
        """Reset the state of the algorithm based on the given state_dict

        :param state_dict: Dictionary representing state of an algorithm
        """
        # TODO: Adapt this to your algo
        self.seed_rng(0)
        self.rng.set_state(state_dict['rng_state'])
        self._trials_info = state_dict.get("_trials_info")

    def suggest(self, num=1):
        """Suggest a `num`ber of new sets of parameters.

        TODO: document how suggest work for this algo

        Parameters
        ----------
        num: int, optional
            Number of points to suggest. Defaults to 1.

        Returns
        -------
        list of points or None
            A list of lists representing points suggested by the algorithm. The algorithm may opt
            out if it cannot make a good suggestion at the moment (it may be waiting for other
            trials to complete), in which case it will return None.

        Notes
        -----
        New parameters must be compliant with the problem's domain `orion.algo.space.Space`.

        """
        # TODO: Adapt this to your algo
        return self.space.sample(num, seed=tuple(self.rng.randint(0, 1000000, size=3)))

    def observe(self, points, results):
        """Observe evaluation `results` corresponding to list of `points` in
        space.

        TODO: document how observe work for this algo

        Parameters
        ----------
        points : list of tuples of array-likes
           Points from a `orion.algo.space.Space`.
           Evaluated problem parameters by a consumer.
        results : list of dicts
           Contains the result of an evaluation; partial information about the
           black-box function at each point in `params`.

        Result
        ------
        objective : numeric
           Evaluation of this problem's objective function.
        gradient : 1D array-like, optional
           Contains values of the derivatives of the `objective` function
           with respect to `params`.
        constraint : list of numeric, optional
           List of constraints expression evaluation which must be greater
           or equal to zero by the problem's definition.

        """
        # TODO: Adapt this to your algo
        pass

    @property
    def is_done(self):
        """Return True, if an algorithm holds that there can be no further improvement."""
        # NOTE: Drop if not used by algorithm
        pass

    def score(self, point):
        """Allow algorithm to evaluate `point` based on a prediction about
        this parameter set's performance.
        """
        # NOTE: Drop if not used by algorithm
        pass

    def judge(self, point, measurements):
        """Inform an algorithm about online `measurements` of a running trial."""
        # NOTE: Drop if not used by algorithm
        pass

    @property
    def should_suspend(self):
        """Allow algorithm to decide whether a particular running trial is still
        worth to complete its evaluation, based on information provided by the
        `judge` method.

        """
        # NOTE: Drop if not used by algorithm
        pass
