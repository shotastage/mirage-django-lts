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
import shutil


def exists(path):
    return os.path.exists(path)


def copy(from_path, to_path, force = False):
    if os.path.exists(to_path):
        if force:
            shutil.rmtree(to_path)
        else:
            raise FileExistsError
            return
    
    shutil.copytree(from_path, to_path)


def move(from_path, to_path, force = False):
    shutil.move(from_path, to_path)


def mkdir(path):
    os.makedirs(path)


def rm(path):
    if os.path.isdir(path): shutil.rmtree(path)
    if os.path.isfile(path): os.remove(path)


def cwd():
    return os.getcwd()


def cd(path):
    os.chdir(path)
