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


def create(proj_author: str, author_email: str, license_url: str) -> str:

    return textwrap.dedent('''
{{
    "miragefile": "v0.0.4",
    "private_profile": {{
        "name": "{PROJECT_AUTHOR}",
        "email": "{PROJECT_AUHOR_EMAIL}"
    }},

    "private_license": {{
        "url": "{LICENSE_DOC_URL}"
    }}
}}

''').format(
    PROJECT_AUTHOR      = proj_author,
    PROJECT_AUHOR_EMAIL = author_email,
    LICENSE_DOC_URL     = license_url,
).strip()
