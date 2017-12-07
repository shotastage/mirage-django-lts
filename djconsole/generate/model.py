# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.

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

from djconsole.flow import Flow
from djconsole.command import log, command
from djconsole.generate.model_template import create_model_py




class DjangoModelMakeFlow(Flow):

    def __init__(self, third_args):
        self._third_args = third_args


    def flow(self):

        model_classies = self._third_args[0]
        model_contents = self._third_args[1:len(self._third_args)]        
        model_body = self.__make_model_body(model_contents)

        modelpy = create_model_py(model_classies, model_body)


        if os.path.isfile("manage.py"):
            log("Please generate model inside the Django app directory.", withError = True)


        try:
            with open("models.py", "a") as writing:
                writing.write(modelpy)
        except:
            log("Failed to open models.py", withError = True)



    def __make_model_body(self, model_contents):

        body = ""

        for content in model_contents:

            data_name = content.split(":")[0]
            data_type = content.split(":")[1]

            try:
                self.___data_name_validator(data_name)
            except:
                log("The data name is invalid!", withError = True)
        

            if "string" == data_type:
                body += '    {0}\n'.format(self.__model_string(data_name))
            elif "text" == data_type:
                body += '    {0}\n'.format(self.__model_text(data_name))
            elif "integer" == data_type:
                body += '    {0}\n'.format(self.__model_integer(data_name))
            elif "date" == data_type:
                body += '    {0}\n'.format(self.__model_date(data_name))
            elif "auto" == data_type:
                body += '    {0}\n'.format(self.__model_auto(data_name))
            else:
                log("Unsuported type " + data_type + ".", withError = True)

        return body



    # Django Char Filed
    def __model_string(self, name):
        return '{0} = models.CharField(max_length=255)'.format(name)

    # Django Long Text Filed
    def __model_text(self, name):
        return '{0} = models.CharField(max_length=65536)'.format(name)

    # Django Integer Filed
    def __model_integer(self, name):
        return '{0} = models.IntegerField()'.format(name)

    # Django Date Filed
    def __model_date(self, name):
        return '{0} = models.DateField()'.format(name)

    # Django Auto Filed
    def __model_auto(self, name):
        return '{0} = models.AutoField(primary_key=True)'.format(name)



    def ___data_name_validator(self, name):
        forbiddens = ["from"]

        for word in forbiddens:
            if name == word:
                raise ValueError("This data name is forbidden.")
