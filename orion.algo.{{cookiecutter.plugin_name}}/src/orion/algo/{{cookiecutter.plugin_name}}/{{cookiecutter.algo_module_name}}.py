# -*- coding: utf-8 -*-
"""
:mod:`orion.algo.{{ cookiecutter.plugin_name }}.{{ cookiecutter.algo_module_name }} -- TODO 
======================{{ '=' * cookiecutter.plugin_name|length }}==================

.. module:: {{ cookiecutter.algo_module_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
from orion.algo.base import BaseAlgorithm


class {{ cookiecutter.algo_name }}(BaseAlgorithm):
    """
    TODO: Class docstring
    """

    def __init__(self, space):
        """
        TODO: init docstring
        """
        super({{ cookiecutter.algo_name }}, self).__init__(space)

    def suggest(self, name=1):
        """Suggest a `num`ber of new sets of parameters.

        TODO: document how suggest work for this algo

        """
        raise NotImplementedError

    def observe(self, points, results):
        """Observe evaluation `results` corresponding to list of `points` in
        space.

        TODO: document how observe work for this algo

        """
        raise NotImplementedError

    @property
    def is_done(self):
        """Return True, if an algorithm holds that there can be no further improvement."""
        # NOTE: Drop if not used by algorithm
        raise NotImplementedError

    def score(self, point):
        """Allow algorithm to evaluate `point` based on a prediction about
        this parameter set's performance.
        """
        # NOTE: Drop if not used by algorithm
        raise NotImplementedError

    def judge(self, point, measurements):
        """Inform an algorithm about online `measurements` of a running trial."""
        # NOTE: Drop if not used by algorithm
        raise NotImplementedError

    @property
    def should_suspend(self):
        """Allow algorithm to decide whether a particular running trial is still
        worth to complete its evaluation, based on information provided by the
        `judge` method.

        """
        # NOTE: Drop if not used by algorithm
        raise NotImplementedError
