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

import yaml
import os
from djconsole import project


class DjConfig():

    def __init__(self):
        self._config = None
        self._load()


    def _load(self):
        if project.in_app():
            os.chdir("../")

        if project.in_project():
            with open("DjFile") as conf:
                self._config = yaml.load(conf)
