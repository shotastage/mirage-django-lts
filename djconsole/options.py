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

from enum import Enum

class DjConsoleOptions(Enum):
    # Create new django application
    dj_new = 1

    # Generate app, model, template, view and so on
    dj_gen = 2

    # Remove app or mtvs
    dj_destory = 3

    # Run Debug Server
    dj_server = 4


class DjGen(Enum):
    app = 1
    model = 2
    template = 3
    view = 4
