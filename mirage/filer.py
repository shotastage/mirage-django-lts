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

import functools
import os
from os import getcwd, chdir
from contextlib import contextmanager


@contextmanager
def chdir(next):
    current = getcwd()
    chdir(next)
    yield
    chdir(current)


def exist(name):
    return os.path.exists(name)


"""
Decorators
"""
def fileexists(*check_file):

    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.isfile(check_file[0]):
                re = func(*args, **kwargs)
                return re
        return wrapper
    return _decorator
