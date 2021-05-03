# -*- coding: utf-8 -*-
# pylint:disable=invalid-name
"""Perform integration tests for `orion.algo.{{ cookiecutter.plugin_name }}`."""
import os
from shutil import which

import numpy
import orion.core.cli
import pytest
from orion.testing.algo import BaseAlgoTests



# Test suite for algorithms. You may reimplement some of the tests to adapt them to your algorithm
# Full documentation is available at https://orion.readthedocs.io/en/stable/code/testing/algo.html
# Look for algorithms tests in https://github.com/Epistimio/orion/blob/master/tests/unittests/algo
# for examples of customized tests.
class Test{{ cookiecutter.algo_name }}(BaseAlgoTests):

    algo_name = {{ cookiecutter.algo_name|lower }}
    config = {
        "seed": 1234,  # Because this is so random
        # Add other arguments for your algorithm to pass test_configuration
    }


# You may add other phases for test.
# See https://github.com/Epistimio/orion.algo.skopt/blob/master/tests/integration_test.py
# for an example where two phases are registered, one for the initial random step, and
# another for the optimization step with a Gaussian Process.
Test{{ cookiecutter.algo_name }}.set_phases(
    [("random", 0, "space.sample")]
)
