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

def src(proj_name, ver, desc, git_url, author, author_email, license_name):

    return textwrap.dedent(
'''
{{
  "name": "{PROJECT_NAME}",
  "version": "{VERSION}",
  "description": "{DESCRIPTION}",
  "repository": "{GIT_REPOSITORY}",
  "author": "{AUTHOR_NAME} <{EMAIL}>",
  "license": "{LICENSE}",
  "private": true,
  "dependencies": {{
    "react": "^16.2.0",
    "react-dom": "^16.2.0",
    "react-redux": "^5.0.6",
    "react-scripts-ts": "2.13.0",
    "redux": "^3.7.2"
  }},
  "scripts": {{
    "start": "react-scripts-ts start",
    "build": "react-scripts-ts build",
    "test": "react-scripts-ts test --env=jsdom",
    "eject": "react-scripts-ts eject"
  }},
  "devDependencies": {{
    "@types/jest": "^22.1.2",
    "@types/node": "^9.4.6",
    "@types/react": "^16.0.38",
    "@types/react-dom": "^16.0.4",
    "typescript": "^2.7.1"
  }}
}}
''').format(
        PROJECT_NAME = proj_name,
        VERSION = ver,
        DESCRIPTION = desc,
        GIT_REPOSITORY = git_url,
        AUTHOR_NAME = author,
        EMAIL = author_email,
        LICENSE = license_name
    ).strip()
