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

def warn(string, warning_class = None):
    if not warning_class == None:
        print('\033[31mMirage (WARNING): {0}\033[0m'.format(str(string)))
    else:
        print('\033[31mMirage ({0}): {1}\033[0m'.format(warning_class.title, str(string)))



"""
Mirage warning classies
"""
class Warning():
    title = "WARNING"

class PendingDeprecationWarning():
    title = "Pending Deprecation"

class DeprecatedWarning():
    title = "Deprecated"

class NotImplementedWarning():
    title = "Not Implemented"

class UnderConstructionWarning():
    title = "Under Construction"

class UnstableFeatureWarning():
    title = "Unstable"
