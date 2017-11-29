#!/usr/bin/env python
# -*- coding: utf-8 -*-

import project
import sys

from options import DjConsoleOptions as cmd_ops

def arg_parser():
    usage = 'Usage: python {} FILE [--verbose] [--cat <file>] [--help]'\
            .format(__file__)

    args = sys.argv
    if len(args) == 1:
        return usage

    # Remove own
    args.pop(0)

    try:
        first_arg = args[0]
    except:
        first_arg = None

    try:
        second_arg = args[1]
    except:
        second_arg = None



    if first_arg == "new":
        return cmd_ops.dj_new

    if first_arg == "g" or first_arg == "generate":
        return cmd_ops.dj_gen



if __name__ == '__main__':
    cmds = arg_parser()

    if cmds == "dj-new":
        project.dj_new_flow()
