"""
:mod:`orion.algo.{{ cookiecutter.plugin_name }}.{{ cookiecutter.algo_module_name }} -- TODO
======================{{ '=' * cookiecutter.plugin_name|length }}==================

TODO: Write long description
"""
import numpy
from orion.algo.base import BaseAlgorithm


class {{ cookiecutter.algo_name }}(BaseAlgorithm):
    """TODO: Class docstring

    Parameters
    ----------
    space: `orion.algo.space.Space`
        Optimisation space with priors for each dimension.
    seed: None, int or sequence of int
        Seed for the random number generator used to sample new trials.
        Default: ``None``

    """

    requires_type = None
    requires_dist = None
    requires_shape = None

    def __init__(self, space, seed=None):
        super({{ cookiecutter.algo_name }}, self).__init__(space, seed=seed)

    def seed_rng(self, seed):
        """Seed the state of the random number generator.

        Parameters
        ----------
        seed: int
            Integer seed for the random number generator.

        """
        # TODO: Adapt this to your algo
        self.rng = numpy.random.RandomState(seed)

    @property
    def state_dict(self):
        """Return a state dict that can be used to reset the state of the algorithm."""
        state_dict = super({{ cookiecutter.algo_name }}, self).state_dict
        # TODO: Adapt this to your algo
        state_dict["rng_state"] = self.rng.get_state()
        return state_dict

    def set_state(self, state_dict):
        """Reset the state of the algorithm based on the given state_dict

        :param state_dict: Dictionary representing state of an algorithm
        """
        # TODO: Adapt this to your algo
        super({{ cookiecutter.algo_name }}, self).set_state(state_dict)
        self.seed_rng(0)
        self.rng.set_state(state_dict["rng_state"])

    def suggest(self, num):
        """Suggest a number of new sets of parameters.

        TODO: document how suggest work for this algo

        Parameters
        ----------
        num: int, optional
            Number of trials to suggest. The algorithm may return less than the number of trials
            requested.

        Returns
        -------
        list of trials or None
            A list of trials representing values suggested by the algorithm. The algorithm may opt
            out if it cannot make a good suggestion at the moment (it may be waiting for other
            trials to complete), in which case it will return None.


        Notes
        -----
        New parameters must be compliant with the problem's domain `orion.algo.space.Space`.

        """
        # TODO: Adapt this to your algo
        trials = []
        while len(trials) < num and not self.is_done:
            seed = tuple(self.rng.randint(0, 1000000, size=3))
            new_trial = self.format_trial(self.space.sample(1, seed=seed)[0])
            if not self.has_suggested(new_trial):
                self.register(new_trial)
                trials.append(new_trial)

        return trials

    def observe(self, trials):
        """Observe the `trials` new state of result.

        TODO: document how observe work for this algo

        Parameters
        ----------
        trials: list of ``orion.core.worker.trial.Trial``
           Trials from a `orion.algo.space.Space`.

        """
        # TODO: Adapt this to your algo or remove if base implementation is fine.
        super({{ cookiecutter.algo_name }}, self).observe(trials)

    @property
    def is_done(self):
        """Return True, if an algorithm holds that there can be no further improvement."""
        # NOTE: Drop if base implementation is fine.
        return super({{ cookiecutter.algo_name }}, self).is_done
