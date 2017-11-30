# -*- coding: utf-8 -*-

import sys
from djconsole.executor import exe
from djconsole.options import DjConsoleOptions as cmd_ops

def arg_parser(first_arg):
    if first_arg == "new":
        return cmd_ops.dj_new

    if first_arg == "g" or first_arg == "generate":
        return cmd_ops.dj_gen

    if first_arg == "s" or first_arg == "server":
        return cmd_ops.dj_server


def main():
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
        second_arg = args[1]
    except:
        second_arg = None


    try:
        third_args = []

        for i in range(len(args) - 2):
            index = i + 2
            third_args.append(args[index])

    except:
        third_args = None


    cmds = arg_parser(first_arg)

    if cmds == cmd_ops.dj_new:
        exe(cmd_ops.dj_new, second_arg, third_args)

    elif cmds == cmd_ops.dj_gen:
        exe(cmd_ops.dj_gen, second_arg, third_args)
    elif cmds == cmd_ops.dj_server:
        exe(cmd_ops.dj_server, second_arg, third_args)
