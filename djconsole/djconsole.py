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

import sys
from djconsole.executor import exe
from djconsole.options import DjConsoleOptions as cmd_ops


def main():
    args = sys.argv
    if len(args) == 1:
        print('Usage: python {} FILE [--verbose] [--cat <file>] [--help]'\
            .format(__file__))

    # Remove own
    args.pop(0)

    try:
        first_arg = args[0]
    except:
        first_arg = None

    try:
        second_arg = args[1]
    except:
        second_arg = None


    try:
        third_args = []

        for i in range(len(args) - 2):
            index = i + 2
            third_args.append(args[index])

    except:
        third_args = None


    exe(first_arg, second_arg, third_args)
