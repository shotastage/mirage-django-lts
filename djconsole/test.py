#!/usr/bin/env python

from enum import Enum

class Opts(Enum):
    new = 1
    gen = 2

class ExeFlow():

    def __init__(self, action, dict):
        self._action = action
        self._opts = dict

    def execute(self):



if __name__ == "__main__":
    exe = ExeFlow("new", { Opts.new: new, Opts.gen: gen })

    def new():
        print("NEW")

    def gen():
        print("NEW")
