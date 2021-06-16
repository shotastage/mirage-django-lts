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

def log(string,
            withError = False, errorDetail = None,
            withInput = False, withConfirm = False, default = None):


    if withError:

        print('\033[31mMirage: ' + str(string) + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =======================================================\n"
            separator_end   = "==========================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')


    elif withInput:
        string = str(input('\033[32m' + str(string) + ' >> \033[0m'))

        if string == "" and default != None:
            return default
        else:
            return string

    elif withConfirm:
        print('\033[31mMirage: ' + str(string) + '\033[0m')

        while True:
            answer = input('\033[32m' + "Please respond with yes or no [Y/N/y/n]" + ' >> \033[0m').lower()

            if answer in [ "y", "Y", "yes", "Yes", "YES", "Yeah"]:
                return True
            elif answer in [ "n", "N", "no", "No", "NO", "Nope"]:
                return False

    else:
        print('\033[32mMirage: \033[0m' + str(string))
