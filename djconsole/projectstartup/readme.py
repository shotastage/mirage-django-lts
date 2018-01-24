import platform
import sys
import django
import textwrap

from pip.utils import get_installed_distributions

def create_readme_doc(name):

    return textwrap.dedent(
'''
# {name}

This is your first Django application.

# Info

## Environment
OS: {os}

## Versions
Django Version: `{django_version}`

Python Version: `{python_version}`

## Installed pip packages
{installed_pip_packages}

''').format(
    name = name,
    os = get_os_name(),
    django_version = get_django_version(),
    python_version = get_python_version(),
    installed_pip_packages = get_pip_list()
).strip()


def get_django_version():
    version = django.VERSION
    return str(version[0]) + "." + str(version[1]) + "." + str(version[2])

def get_python_version():
    version = sys.version_info
    return str(version[0]) + "." + str(version[1]) + "." + str(version[2])

def get_os_name():
    os = platform.system()

    if os == "Darwin":
        return "macOS"
    elif os == "Windows":
        return os
    else:
        return os

def get_pip_list():
    string = ""

    ignore_packages = ["setuptools", "pip", "python", "djconsole"]
    
    packages = get_installed_distributions(local_only = True, skip = ignore_packages)
    
    for package in packages:
        string += "+ " + package.project_name + " " + package.version + "  \n"

    return string
