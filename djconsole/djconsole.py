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

import sys

from djconsole.djargparse import ArgumentsParser

# For Driver
from djconsole.executor_driver import GatheredArgsDriver
from djconsole.executor_driver import new, cms_new, generate



def main():

    parser = ArgumentsParser(
        usage = """
Django Console v0.0.11


    new             Create a new Django project
    new:cms         Create a new Django CMS project
    new:api         Create a new Django REST API

    generate / g    Generate apps, model
        + app       Generate Django app
        + model     Generate Django model class
                """,

        version = """
Django Console Version 0.0.12

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
                  """
    )

    # For arg parse v1 driver
    action_handler = GatheredArgsDriver(parser._cmd, parser._option, parser._values)
    action = parser._cmd


    # Driving commands
    parser.add_argument("new", "new_application", None, lambda: new(action_handler, action))
    parser.add_argument_with_subaction("new", "new_application", "cms", None, lambda: cms_new(action_handler, action))
    parser.add_argument("g", "generate", "app", generate(action_handler, action))
    parser.add_argument("g", "generate", "model", generate(action_handler, action))


    # Commands
    parser.add_argument("tf", "testfunc", None, test_func)
    parser.add_argument_with_subaction("tfs", "testfuncs", "exec", None, test_func)


    # Excute
    parser.parse()


# For test
def test_func(cmd, action, option, detail_option, values):
    print("Yeah!")
    print(str(cmd))
    print(str(action))
    print(str(option))
    print(str(detail_option))
    print(str(values))
