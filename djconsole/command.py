import os
import inspect
import sys
import textwrap
import functools
from subprocess import check_output, DEVNULL, STDOUT


def log(string, withError = False, withExitOnError = False, errorDetail = None, withInput = False):
    if withError:
        print('\033[31mDjango Console: ' + string + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =======================================================\n"
            separator_end   = "==========================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')

        if withExitOnError:
            sys.exit(1)

    elif withInput:
        return input('\033[32m' + string + ' >> \033[0m')

    else:
        print('\033[32mDjango Coneole: \033[0m' + string)



def raise_error_message(func):

    errored_func = func.__name__
    errored_obj  = str(func)

    return textwrap.dedent("""
Python Information:

Excute func name : {func_name}
Object Info      : {obj_inf}
    """).format(
        func_name = errored_func,
        obj_inf   = errored_obj
    ).strip()


def command(command, withOutput = False):
    separated_cmds = command.split(" ")

    if withOutput:
        try:
            check_output(separated_cmds, stderr=STDOUT)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)

    else:
        try:
            check_output(separated_cmds, stderr=DEVNULL)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)


def reserve_as_command(*reserved_args):

    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for reserve in reserved_args:
                if args[1] == reserve:
                    re = func(*args, **kwargs)
                    return re
        return wrapper
    return _decorator
