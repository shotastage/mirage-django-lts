import os
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

from mirage.flow    import Flow
from mirage.manual  import info


class DjangoVersionFlow(Flow):

    def flow(self):
        self.log("Django Console")
        self.log("Version " + info.version + " build " + info.build)
    

    def log(self, string):
        print('\033[32m\033[0m' + string)
