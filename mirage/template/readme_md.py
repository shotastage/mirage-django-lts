# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import platform
import sys
import textwrap

try: # pip >= 10
    from pip._internal.utils.misc import get_installed_distributions
except ImportError:  # pip < 10
    from pip import get_installed_distributions

from mirage.command import log


def src(name, desc = "No description provided."):

    return textwrap.dedent(
'''
# {NAME}

{DESCRIPTION}

# Info
Information of development environment.

## Environment
OS: {OS}

## Versions
Django Version: `{DJANGO_VER}`

Python Version: `{PYTHON_VER}`

## Installed pip packages
{INSTALLED_PIP_PACKAGES}

''').format(
    NAME = name,
    OS = get_os_name(),
    DJANGO_VER = get_django_version(),
    PYTHON_VER = get_python_version(),
    INSTALLED_PIP_PACKAGES = get_pip_list(),
    DESCRIPTION = desc,
).strip()


def get_django_version():
    try:
        import django
        version = django.VERSION
        return str(version[0]) + "." + str(version[1]) + "." + str(version[2])
    except:
        log("Failed to import Django!", withError = True)
        return "FAILED TO IMPORT DJANGO!"


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

    ignore_packages = ["setuptools", "pip", "python", "mirage"]

    packages = get_installed_distributions(local_only = True, skip = ignore_packages)

    for package in packages:
        string += "+ " + package.project_name + " " + package.version + "  \n"

    return string
