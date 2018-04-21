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

from mirage.core import Void
from mirage.flow import Workflow
from mirage.help import description, description_long

class UsageShowWorkFlow(Workflow):

    def main(self) -> Void:
        if self._option == "--detail":
            print(description_long.usage_doc())
        else:
            print(description.usage_doc())


class VersionShowWorkFlow(Workflow):

    def main(self) -> Void:
        print(description.version_doc())
