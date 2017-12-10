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

from djconsole.flow                     import Flow
from djconsole.command                  import log, command
from djconsole.generate.model_template  import create_model_py



class DjangoModelMakeFlow(Flow):

    def __init__(self, third_args):
        self._third_args = third_args


    def flow(self):

        model_classies = self._third_args[0]
        model_contents = self._third_args[1:len(self._third_args)]        
        model_body     = self.__make_model_body(model_contents)

        modelpy = create_model_py(model_classies, model_body)


        if os.path.isfile("manage.py"):
            log("Please generate model inside the Django app directory.", withError = True)


        try:
            with open("models.py", "a") as writing:
                writing.write(modelpy)
        except:
            log("Failed to open models.py", withError = True)



    def __make_model_body(self, model_contents):
        """
        Make model body from model contents string
        :param self:
        :param model_contents: String     Model contents represantation
        :return: String                   Model body as string
        """

        body = ""

        for content in model_contents:

            data_name = content.split(":")[0]  # model filed name
            data_type = content.split(":")[1]  # data type
            data_args = content.split(":")[2]  # filed arguments


            # Validate data filed names
            try:
                self.___data_name_validator(data_name)
            except:
                log("The data name is invalid!", withError = True)


            # Get arguments string
            args = self.__make_argumanets(data_args)

           
            # Make model body
            if "string"    == data_type:
                body += '    {0}\n'.format(self.__model_string(
                                                            data_name, args))
            elif "text"    == data_type:
                body += '    {0}\n'.format(self.__model_text(
                                                            data_name, args))
            elif "integer" == data_type:
                body += '    {0}\n'.format(self.__model_integer(
                                                            data_name, args))
            elif "boolean" == data_type:
                body += '    {0}\n'.format(self.__model_boolean(
                                                            data_name, args))
            elif "date"    == data_type:
                body += '    {0}\n'.format(self.__model_date(
                                                            data_name, args))
            elif "auto"    == data_type:
                body += '    {0}\n'.format(self.__model_auto(
                                                            data_name, args))
            else:
                log("Unsuported type " + data_type + ".", withError = True)

        return body
    


    # Django string filed
    def __model_string(self, name, arg_filed):
        return '{0} = models.CharField(max_length=255, {1})'.format(name, arg_filed)

    # Django Long Text Filed
    def __model_text(self, name, arg_filed):
        return '{0} = models.CharField(max_length=65536, {1})'.format(name, arg_filed)

    # Django Integer Filed
    def __model_integer(self, name, arg_filed):
        return '{0} = models.IntegerField({1})'.format(name, arg_filed)

    # Django Boolean Filed
    def __model_boolean(self, name, arg_filed):
        return '{0} = models.BooleanField({1})'.format(name, arg_filed)

    # Django Date Filed
    def __model_date(self, name, arg_filed):
        return '{0} = models.DateField({1})'.format(name, arg_filed)

    # Django Auto Filed
    def __model_auto(self, name, arg_filed):
        return '{0} = models.AutoField(primary_key=True, {1})'.format(name, arg_filed)



    def __make_argumanets(self, arg_propaties):
        
        args = arg_propaties.split(",")
        arg_text = ""

        for arg in args:
            arg_text += " " + ""

        return arg_text


    def ___data_name_validator(self, name):
        forbiddens = ["from"]

        for word in forbiddens:
            if name == word:
                raise ValueError("This data name is forbidden.")
