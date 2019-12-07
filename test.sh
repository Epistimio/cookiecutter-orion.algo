#!/usr/bin/env bash

rm -rf orion.algo.my_plugin

virtualenv test-cookiecutter
source test-cookiecutter/bin/activate

python -m pip install 'cookiecutter>=1.5' 'versioneer>=0.18' jinja2

cookiecutter . -vvv --no-input \
    plugin_name=my_plugin \
    author_name="John Doe" \
    author_short="John Doe" \
    author_email="john@doe.com" \
    github_username="johndoe" \
    copyright="2019, John Doe" \
    short_description="Config to test cookicutter template" \
    synopsis="Random Algo" \
    algo_name="SuperDupperAlgo" \
    algo_module_name="super_dupper_algo"

cd orion.algo.my_plugin
pip install -r dev-requirements.txt
tox -e flake8
tox -e pylint
tox -e py36
tox -e benchmark
cd ..

rm -rf test-cookiecutter
