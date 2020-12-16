#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint:disable=invalid-name
"""Perform integration tests for `orion.algo.{{ cookiecutter.plugin_name }}`."""
import os

import numpy
import orion.core.cli
import pytest
from orion.algo.space import Integer, Real, Space
from orion.client import create_experiment
from orion.core.utils.tests import OrionState
from orion.core.worker.primary_algo import PrimaryAlgo


# pylint:disable=unused-argument
def rosenbrock_function(x, y):
    """Evaluate a n-D rosenbrock function."""
    z = x - 34.56789
    r = 4 * z ** 2 + 23.4
    return [dict(name="objective", type="objective", value=r)]


@pytest.fixture()
def space():
    """Return an optimization space"""
    space = Space()
    dim1 = Integer("yolo1", "uniform", -3, 6)
    space.register(dim1)
    dim2 = Real("yolo2", "uniform", 0, 1)
    space.register(dim2)

    return space


def test_seeding(space):
    """Verify that seeding makes sampling deterministic"""
    optimizer = PrimaryAlgo(space, "{{ cookiecutter.algo_name|lower }}")

    optimizer.seed_rng(1)
    a = optimizer.suggest(1)[0]
    with pytest.raises(AssertionError):
        numpy.testing.assert_equal(a, optimizer.suggest(1)[0])

    optimizer.seed_rng(1)
    numpy.testing.assert_equal(a, optimizer.suggest(1)[0])


def test_set_state(space):
    """Verify that resetting state makes sampling deterministic"""
    optimizer = PrimaryAlgo(space, "{{ cookiecutter.algo_name|lower }}")

    optimizer.seed_rng(1)
    state = optimizer.state_dict
    a = optimizer.suggest(1)[0]
    with pytest.raises(AssertionError):
        numpy.testing.assert_equal(a, optimizer.suggest(1)[0])

    optimizer.set_state(state)
    numpy.testing.assert_equal(a, optimizer.suggest(1)[0])


def test_optimizer_basic(monkeypatch):
    """Check functionality of BayesianOptimizer wrapper for single shaped dimension."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~uniform(-5, 5)",
            ]
        )


def test_int(monkeypatch):
    """Check support of integer values."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~uniform(-5, 5, discrete=True)",
            ]
        )


def test_categorical(monkeypatch):
    """Check support of categorical values."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~choices([-5, -2, 0, 2, 5])",
            ]
        )


def test_linear(monkeypatch):
    """Check support of logarithmic distributions."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~loguniform(1, 50, discrete=True)",
            ]
        )


def test_shape(monkeypatch):
    """Check support of multidim values."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~uniform(-5, 5, shape=3)",
            ]
        )


def test_optimizer_two_inputs(monkeypatch):
    """Check functionality of BayesianOptimizer wrapper for 2 dimensions."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "-x~uniform(-5, 5)",
                "-y~uniform(-10, 10)",
            ]
        )


def test_optimizer_actually_optimize(monkeypatch):
    """Check if Bayesian Optimizer has better optimization than random search."""
    monkeypatch.chdir(os.path.dirname(os.path.abspath(__file__)))
    best_random_search = 23.403275057472825

    with OrionState(experiments=[], trials=[]):

        orion.core.cli.main(
            [
                "hunt",
                "--config",
                "./benchmark/{{ cookiecutter.algo_name|lower }}.yaml",
                "./benchmark/rosenbrock.py",
                "--max-trials",
                100,
                "-x~uniform(-50, 50)",
            ]
        )

        exp = create_experiment(name="exp")

        objective = exp.stats["best_evaluation"]

        assert best_random_search > objective
