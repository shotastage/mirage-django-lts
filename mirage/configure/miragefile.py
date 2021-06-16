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

import textwrap


def create_djfile(name, version, author, git_url, license, description, dj_app_path, python_pkg_m, default_db, 
    front_app_path, front_pkg_m, front_app_builder, workspace_path):

    return textwrap.dedent(
'''
project:
    name: {app_name}
    version: {version}
    author: {author}
    git: {git_url}
    license: {license}
    description: {description}

django:
    path: {django_app_path}
    package: {python_package_m}
    database: {default_database}

frontend:
    path: {front_app_path}
    package: {front_package_manager}
    builder: {front_app_builder}

djworkspace:
    path: {workspace_path}

''').format(
    app_name = name,
    version = version,
    author = author,
    git_url = git_url,
    license = license,
    description = description,
    django_app_path = dj_app_path,
    python_package_m = python_pkg_m,
    default_database = default_db,
    front_app_path = front_app_path,
    front_package_manager = front_pkg_m,
    front_app_builder = front_app_builder,
    workspace_path = workspace_path
).strip()



def create_additional(options):
    return textwrap.dedent(
'''
additional_options:
    {options}
''').format(
    options = options
).strip()
