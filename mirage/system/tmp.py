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

import contextlib
import uuid
import os

from mirage import fileable


@contextlib.contextmanager
def tmpWorking(tmp_name):

    # Directories
    working = tmp_name + uuid.uuid4()
    current = os.getcwd()
    
    # Enter
    fileable.mkdir(working)
    os.chdir(working)
    yield

    # Exit
    os.chdir(current)
    fileable.rm(working)
