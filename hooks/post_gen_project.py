"""
Does the following:
1. Deletes requirements.txt if not needed
2. Deletes packer if not going to be used
3. Inits git
"""
from __future__ import print_function
import os
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def remove_molecule_file(filename):
    """
    generic remove file from molecule dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, "molecule", "default", filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)

def init_git():
    """
    Initialises git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "initial commit"]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()

# 1. Remove requirements.yml if the role has not dependencies
if '{{ cookiecutter.role_has_dependency }}' == 'no':
    remove_molecule_file("requirements.yml")

# 2. Remove packer.json if packer is not going to be used
if '{{ cookiecutter.deploy_role }}' == 'no':
    remove_file("packer.json")

# 3. Initialize Git
if '{{ cookiecutter.init_git }}' == 'yes':
    init_git()