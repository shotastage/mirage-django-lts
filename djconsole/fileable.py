# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
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
    shutil.rmtree(path)


def cwd():
    return os.getcwd()


def cd(path):
    os.chdir(path)
