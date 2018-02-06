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

def create_package_json(proj_name, ver, desc, git_url, author, author_email, license_name):

    return textwrap.dedent(
'''
{
  "name": "{project_name}-shell",
  "version": "{version}",
  "description": "{description}",
  "main": "index.js",
  "repository": "{git_repository}",
  "author": "{author_name} <{email}>",
  "license": "{license_type}"
}
''').format(
        project_name = proj_name,
        version = ver,
        description = desc,
        git_repository = git_url,
        author_name = author,
        email = author_email,
        license_type = license_name
    ).strip()
