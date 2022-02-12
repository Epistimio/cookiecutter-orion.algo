""" Test the orion algo Cookiecutter template.

A template project is created in a temporary directory, the application is
installed into a self-contained venv environment, and the application test 
suite is run.

"""
from contextlib import contextmanager
from json import load
from os import chdir
from os.path import abspath
from os.path import dirname
from os.path import join
from shlex import split
from shutil import which
from subprocess import check_call
from tempfile import TemporaryDirectory
from venv import create

from cookiecutter.main import cookiecutter


config = dict(
    plugin_name="test_plugin",
    author_name="John Doe",
    author_short="John Doe",
    author_email="john@doe.com",
    github_username="johndoe",
    algo_name="TestAlgo",
    algo_module_name="test_algo",
)


def main():
    """Execute the test."""
    template = dirname(dirname(abspath(__file__)))
    defaults = load(open(join(template, "cookiecutter.json")))
    with TemporaryDirectory() as tmpdir:
        chdir(tmpdir)
        check_call(split("ls -la"))
        cookiecutter(template, no_input=True, extra_context=config)
        chdir(join(tmpdir, f"orion.algo.{config['plugin_name']}"))
        create("venv", with_pip=True)
        path = join("venv", "bin")
        pip = which("pip", path=path) or "pip"  # GH CI workaround
        check_call(split(f"{pip} install -e ."))
        check_call(split(f"{pip} install -r dev-requirements.txt"))
        check_call(split(f"{pip} install -r tests/requirements.txt"))
        pytest = which("pytest", path=path) or "pytest"  # GH CI workaround
        test = "{:s} -vv tests -x".format(pytest)
        tox = which("tox", path=path) or "tox"  # GH CI workaround
        test = "{:s} -e black".format(tox)
        check_call(split(test))
        test = "{:s} -e isort".format(tox)
        check_call(split(test))
        test = "{:s} -e pylint".format(tox)
        check_call(split(test))
    return 0


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
