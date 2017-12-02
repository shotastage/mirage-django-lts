# -*- coding: utf-8 -*-

import sys
from djconsole.executor import exe
from djconsole.options import DjConsoleOptions as cmd_ops


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


    exe(first_arg, second_arg, third_args)
