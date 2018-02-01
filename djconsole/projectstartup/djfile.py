# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

import platform
import sys
import textwrap

from pip.utils import get_installed_distributions
from djconsole.command import log


def create_djfile(name, version, author, git_url, license):

    return textwrap.dedent(
'''
app:
    name: {app_name}
    version: {version}
    author: {author}
    git: {git_url}
    license: {license}
django:
    path: .
    package: pipenv
frontend:
    path: shell
    package: yarn
djworkspace:
    path: .djc
''').format(
    app_name = name,
    version = version,
    author = author,
    git_url = git_url,
    license = license
).strip()
