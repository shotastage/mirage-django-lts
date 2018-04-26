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
import datetime


def create(proj_name, proj_ver, proj_author, author_email, git_url,
                                        proj_license, proj_desc, copyrightor):

    return textwrap.dedent('''
{{
    "miragefile": "v0.0.4",
    
    "project": {{
        "name": "{PROJECT_NAME}",
        "version": "{PROJECT_VERSION}",
        "author": "{PROJECT_AUTHOR} <{PROJECT_AUHOR_EMAIL}>",
        "git": "{GIT_URL}",
        "license": "{PROJECT_LICENSE}",
        "description": "{PROJECT_DESC}",

        "django": {{
            "path": ".",
            "module": "{MODULE_NAME}",
            "package": "pipenv",
            "database": "PostgreSQL"
        }},

        "frontend": {{
            "path": "shell",
            "package": "yarn",
            "builder": "webpack"
        }},

        "workspace": {{
            "path": ".mirage"
        }},

        "copyright": {{
            "start_year": {COPYRIGHT_START},
            "copyrightors": [
                "{COPYRIGHTOR}"
            ]
        }}
    }}
}}

''').format(
    PROJECT_NAME        = proj_name,
    PROJECT_VERSION     = proj_ver,
    PROJECT_AUTHOR      = proj_author,
    PROJECT_AUHOR_EMAIL = author_email,
    GIT_URL             = git_url,
    PROJECT_LICENSE     = proj_license,
    PROJECT_DESC        = proj_desc,
    MODULE_NAME         = proj_name,
    COPYRIGHT_START     = get_start_year(),
    COPYRIGHTOR         = copyrightor
).strip()


def get_start_year():
    return datetime.datetime.now().strftime("%Y")
