#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil
import subprocess

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

# DOCS_SOURCES = "docs_sources"
# ALL_TEMP_FOLDERS = [DOCS_SOURCES, "licenses", "macros"]
ALL_TEMP_FOLDERS = ["macros"]
DOCS_FILES_BY_TOOL = {
    "mkdocs": ["index.md", "/mkdocs.yml"],
    "sphinx": ["conf.py", "index.rst", "make.bat", "Makefile"],
}


def move_docs_files(docs_tool, docs_files, docs_sources):
    if docs_tool == "none":
        return

    root = os.getcwd()
    docs = "docs"

    logger.info("Initializing docs for %s", docs_tool)
    if not os.path.exists(docs):
        os.mkdir(docs)

    for item in docs_files[docs_tool]:
        dst, name = (root, item[1:]) if item.startswith("/") else (docs, item)
        src_path = os.path.join(docs_sources, docs_tool, name)
        dst_path = os.path.join(dst, name)

        logger.info("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


def init_vcs():
    subprocess.run("git init", shell=True, check=True)
    subprocess.run("git add --all", shell=True, check=True)


def run_versioneer():
    subprocess.run("versioneer install", shell=True, check=True)
    subprocess.run("git commit -m 'Creation with cookiecutter'", shell=True, check=True)


def blackify():
    subprocess.run("black .", shell=True, check=True)
    subprocess.run("git commit -a -m 'Format with black'", shell=True, check=True)


if __name__ == "__main__":
    # move_docs_files("\{\{cookiecutter.docs_tool\}\}", DOCS_FILES_BY_TOOL, DOCS_SOURCES)
    remove_temp_folders(ALL_TEMP_FOLDERS)
    init_vcs()
    run_versioneer()
    blackify()
