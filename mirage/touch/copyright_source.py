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

import datetime
import textwrap
from functools import lru_cache


@lru_cache(maxsize = 10)
def copyright_script_style_doc(proj_name, fname, your_name, start, copyrightors, license, license_url) -> str:
    return textwrap.dedent('''
"""
{PROJECT_NAME}
{FILE_NAME}

Created by {YOUR_NAME} on {CURRENT}

{COPYRIGHTS}
This software is released under the terms of {LICENSE_NAME}, see LICENSE for detail.
{LICENSE_URL}
"""

# Import Library

# Code Here

    ''').format(
        PROJECT_NAME = proj_name,
        FILE_NAME = fname,
        YOUR_NAME = your_name,
        START_YEAR = start,
        CURRENT = get_current(),
        COPYRIGHTS = gen_copyrights(start, get_current_year(), copyrightors),
        LICENSE_NAME = license,
        LICENSE_URL = license_url
    ).strip()



@lru_cache(maxsize = 10)
def copyright_c_style_doc(proj_name, fname, your_name, start, copyrightors, license, license_url) -> str:
    return textwrap.dedent('''
/*
{PROJECT_NAME}
{FILE_NAME}

Created by {YOUR_NAME} on {CURRENT}

{COPYRIGHTS}
This software is released under the terms of {LICENSE_NAME}, see LICENSE for detail.
{LICENSE_URL}
*/

// Code Here

    ''').format(
        PROJECT_NAME = proj_name,
        FILE_NAME = fname,
        YOUR_NAME = your_name,
        START_YEAR = start,
        CURRENT = get_current(),
        COPYRIGHTS = gen_copyrights(start, get_current_year(), copyrightors),
        LICENSE_NAME = license,
        LICENSE_URL = license_url
    ).strip()




@lru_cache(maxsize = 10)
def get_current() -> str:
    return datetime.datetime.now().strftime("%Y/%m/%d")

@lru_cache(maxsize = 10)
def get_current_year() -> str:
    return datetime.datetime.now().strftime("%Y")


@lru_cache(maxsize = 10)
def gen_copyrights(start: int, current: int, copyrightors: tuple) -> str:

    string = ""

    if str(start) == str(current):
        for copyrightor in copyrightors:
            string += "Copyright (c) {0} {1} All Rights Reserved.\n".format(current, copyrightor)
    else:
        for copyrightor in copyrightors:
            string += "Copyright (c) {0}-{1} {2} All Rights Reserved.\n".format(start, current, copyrightor)

    return string
