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

from djconsole.djargparse import ArgumentsParser, ParsingStrategies, compatible_with_argparse



def main():

    parser = ArgumentsParser(
        usage = """
Django Console
                """,
        version = """
Django Console Version 0.0.12

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
                  """
    )
