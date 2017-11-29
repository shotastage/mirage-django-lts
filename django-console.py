#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from executor import exe
from options import DjConsoleOptions as cmd_ops

def arg_parser(first_arg):
    if first_arg == "new":
        return cmd_ops.dj_new

    if first_arg == "g" or first_arg == "generate":
        return cmd_ops.dj_gen



if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('Usage: python {} FILE [--verbose] [--cat <file>] [--help]'\
            .format(__file__))

    # Remove own
    args.pop(0)

    try:
        first_arg = args[0]
    except:
        first_arg = None

    try:
        second_arg = []
        second_arg.append(args[1])
    except:
        second_arg = []

    cmds = arg_parser(first_arg)


    if cmds == cmd_ops.dj_new:
        print("HHH")
        exe(cmd_ops.dj_new, second_arg)
