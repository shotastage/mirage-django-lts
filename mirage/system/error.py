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

import inspect
import textwrap
import sys


def raise_error_message(func, e = "No traceback"):

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
{trace_log}
    """).format(
        func_name = errored_func,
        exec_info = exec_info,
        obj_inf   = errored_obj,
        func_signature = func_sig,
        trace_log = e,
    ).strip()
