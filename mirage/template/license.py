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

import enum
from . import licenses


class LicenseTextSource(enum.Enum):
    AGPLv3      = licenses.agpl_v3.text
    Apachae2    = licenses.apache_v2.text
    GPLv3       = licenses.gpl_v3.text
    LGPLv3      = licenses.lgpl_v3.text
    MIT         = licenses.mit.text
    MPLv2       = licenses.mpl_v2.text
    Unlicensed  = licenses.unlicense.text


def src(license_enum):
    return license_enum
