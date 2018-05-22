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

import sys, os, imp
from enum import Enum

class Settings(Enum):

    class License(Enum):
        Original = "Original"
        MIT = "MIT"
        GPL = "GPL"
        AGPL = "AGPL"
        Apache = "Apache"
        EULA = "EULA"


    class PackageManager(Enum):
        default = "pipenv"
        pipenv = "pipenv"
        pip = "pip"
        easy_install = "easy_install"
        yarn = "yarn"


    class Builder(Enum):
        Webpack = "webpack"


    class Database(Enum):
        default = "PostgreSQL"
        PostgreSQL = "PostgreSQL"
        MySQL = "MySQL"
        MariaDB = "MariaDB"

    class Path(Enum):
        default = "shell"
