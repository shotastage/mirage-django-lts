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
import time

class Progress():

    def __init__(self):
        self._current_text = ""

    def write(self, string, withLazy = False):

        # Update
        self._current_text = str(string)

        # Log
        sys.stdout.write('\r' + '\033[32mMirage: \033[0m' + str(self._current_text))

        # Lazy
        if withLazy: time.sleep(0.5)

    def update(self, string, withLazy = False):

        # Clear
        sys.stdout.flush()
        sys.stdout.write("\r{0}".format("                                                                               "))
        sys.stdout.flush()

        self.write(string, withLazy)

    def clear(self):
        sys.stdout.flush()
        sys.stdout.write("\r{0}".format("                                                                               "))
