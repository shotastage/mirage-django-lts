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
import inspect
import warnings
import sys
import textwrap
import functools
from subprocess import check_output, DEVNULL, STDOUT


def log(string,
            withError = False, withExitOnError = False, errorDetail = None,
            withInput = False, withConfirm = False):


    if withError:

        print('\033[31mDjango Console: ' + str(string) + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =======================================================\n"
            separator_end   = "==========================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')

        if withExitOnError:
            warnings.warn(
            "command.log with withExitOnError will be depricated on next version!",
            PendingDeprecationWarning)
            sys.exit(1)

    elif withInput:
        return input('\033[32m' + str(string) + ' >> \033[0m')

    elif withConfirm:
        print('\033[31mDjango Console: ' + str(string) + '\033[0m')

        while True:
            answer = input('\033[32m' + "Please respond with yes or no [Y/N/y/n]" + ' >> \033[0m').lower()

            if answer in [ "y", "Y", "yes", "Yes", "YES", "Yeah"]:
                return True
            elif answer in [ "n", "N", "no", "No", "NO", "Nope"]:
                return False        
    else:
        print('\033[32mDjango Coneole: \033[0m' + str(string))



def raise_error_message(func):

    try:
        errored_func = func.__name__
    except:
        errored_func = "Failed to get func information!"

    try:
        errored_obj  = str(func)
    except:
        errored_obj  = "Failed to get errored object information!"

    try:
        func_sig     = inspect.signature(func)
    except:
        func_sig     = "Failed to get functino signature!"

    try:
        exec_info    = str(sys.exc_info())
    except:
        exec_info    = "Failed to get exec info!"


    return textwrap.dedent("""
Python Information:

Exceute func name : {func_name}
Exec Information  : {exec_info}
Object Info       : {obj_inf}
Signature         : {func_signature}
    """).format(
        func_name = errored_func,
        exec_info = exec_info,
        obj_inf   = errored_obj,
        func_signature = func_sig
    ).strip()



def command(command, withOutput = False):
    separated_cmds = command.split(" ")

    if withOutput:
        try:
            check_output(separated_cmds, stderr=STDOUT)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)

    else:
        try:
            check_output(separated_cmds, stderr=DEVNULL)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)
