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
from mirage.flow import Flow, Workflow
from mirage.command import log, command
from .model_template import create_model_py


class DjangoModelMakeWorkflow(Workflow):

    def additional_init_(self):
        self._model_name = self._values[0]
        self._values.pop(0)
        self._data = self._values

    def main(self):
        # ModelClass name:string<<maxlen=40 no:integer<<as_primary=True

        model_contents = ""
        
        for data in self._data:
            model_contents += self._parse_data(data)
            
        # Write model file
        


    def _parse_data(self, data_string):
        # data_name:data_type+option=value,option=value
        # ex. name:string+maxlen=100,as_primary=True
        data_name = data_string.split(":")[0]
        data_type = self._parse_data_type(data_string)
        data_options = self._parse_option(data_string)
        
        return self._make_col(data_name, data_type, data_options)


    def _parse_data_type(self, data_string):
        if "+" in data_string:
            return data_string.split(":")[1].split("+")[0]
        else:
            return data_string.split(":")[1]


    def _parse_option(self, data_string):
        if "+" in data_string:
            options = data_string.split("+")[1].split(",")

            options_parsed = []

            for option in options:
                option_name = option.split("=")[0]
                option_value = option.split("=")[1]

                options_parsed.append((option_name, option_value))
            
            return options_parsed
        else:
            return None


    def _make_col(self, name, type, ops):
        string = "  {0} = {1}({2})".format(name, self._make_filed(type), self._make_option(type, ops))

        return string


    def _make_filed(self, type):
        if type == "string":
            return "models.CharField"
        elif type == "text":
            return "models.CharField"
        elif type == "integer" or type == "int":
            return "models.IntegerField"
        elif type == "date":
            return "models.DateField"
        elif type == "auto":
            return "models.AutoField"

    def _make_option(self, type, ops):

        opstring = ""

        if ops == None: return ""
        
        # Max len check
        text_is_maxlen = False
        for op in ops:
            if "maxlen" in op[0]: text_is_maxlen = True
            
        #
        for op in ops:
            if type == "string" and text_is_maxlen == False:
                opstring += "max_length = 255"
            elif type == "text" and text_is_maxlen == False:
                opstring += "max_length = 65536"
            elif op[0] == "maxlen":
                opstring += "max_length = {0}".format(op[1])
            elif op[0] == "asprimary":
                opstring += "as_primary = True"
            else:
                opstring += ""

            if not op[0] == ops[len(ops) - 1][0]:
                opstring += ", "

        return opstring
