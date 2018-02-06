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

import os
import enum
from djconsole.flow                     import Flow, Workflow
from djconsole.command                  import log, command
from djconsole.generate.model_template  import create_model_py


class DjangoModelMakeWorkflow(Workflow):

    def additional_init_(self):
        self._model_name = self._values[0]
        self._data = self._values[1:]

    def main(self):
        # ModelClass name:string<maxlen=40> no:integer<as_primary>
        pass

    def _parse_data(self, data_string):
        # data_name:data_type<option=value,option=value>
        # ex. name:string<<maxlen=100,as_primary=True
        data_name = data_string.split(":")[0]
        data_type = self._parse_data_type(data_string)


    def _parse_data_type(self, data_string):
        if "<<" in data_string:
            return data_string.split(":")[1].split("<<")[0]
        else:
            return data_string.split(":")[1]


    def _parse_option(self, data_string):
        pass
