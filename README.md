cookiecutter-ansible
===================

Powered by Cookiecutter, cookiecutter-ansible is the easiest way to setup new ECS Automation projects.

## Features

- creates a Molecule scenario with the default driver (Docker)
- defines basic Ansible Galaxy metadata
- uses Packer for building ECS base images
- uses TravisCI for running molecule test and deploying a new ECS image

Requirements
------------

Install Cookiecutter with pip:
`$ pip install cookiecutter`

alternatively you can use homebrew:
`$ brew install cookiecutter`

Usage
-----
`$ cookiecutter https://github.com/entercloudsuite/cookiecutter-ansible.git`  

You will be asked about the role info (name, service, default port, etc.). This info will be used to customize your new role.  
Warning: a folder with the same name of the role will be created.

License
-------
MIT
