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


def main():

    parser = ArgumentsParser()

    # Driving commands
    parser.add_argument("new", "new_application", None, "DjangoStartup")

    #
    parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", "version", None, "VersionShow")

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
