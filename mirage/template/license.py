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
from . import licensedoc


class LicenseTextSource(enum.Enum):
    AGPLv3      = licensedoc.agpl_v3.src("", "")
    Apachae2    = licensedoc.apache_v2.src("", "")
    GPLv3       = licensedoc.gpl_v3.src("", "")
    LGPLv3      = licensedoc.lgpl_v3.src("", "")
    MIT         = licensedoc.mit_license.src("", "")
    MPLv2       = licensedoc.mpl_v2.src("", "")
    Unlicensed  = licensedoc.unlicense.src("", "")


def src(license_enum):
    return license_enum
