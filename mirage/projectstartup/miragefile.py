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

from pip.utils import get_installed_distributions
from mirage.command import log


def create_djfile(name, version, author, email, git_url, license, description):

    return textwrap.dedent(
'''
project:
    name: {APP_NAME}
    version: {VERSION}
    author: {author} <{EMAIL}>
    git: {GIT_URL}
    license: {LICENSE}
    description: {DESCRIPTION}

django:
    path: .
    package: pipenv
    database: PostgreSQL

frontend:
    path: shell
    package: yarn
    builder: webpack

djworkspace:
    path: .mirage

''').format(
    APP_NAME = name,
    VERSION = version,
    author = author,
    EMAIL = email,
    GIT_URL = git_url,
    LICENSE = license,
    DESCRIPTION = description
).strip()
