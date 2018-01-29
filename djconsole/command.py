import os
import inspect
import warnings
import sys
import textwrap
import functools
from subprocess import check_output, DEVNULL, STDOUT


def log(string,
            withError = False, withExitOnError = False, errorDetail = None,
            withInput = False, withConfirm = False):
    if withError:
        print('\033[31mDjango Console: ' + string + '\033[0m')

        if not errorDetail == None:
            separator_begin = "===== Error Detail =======================================================\n"
            separator_end   = "==========================================================================\n"
            print('\033[31m' + separator_begin + errorDetail + "\n" + separator_end + '\033[0m')

        if withExitOnError:
            warnings.warn(
            "command.log with withExitOnError will be depricated on next version!",
            PendingDeprecationWarning)
            sys.exit(1)

    elif withInput:
        return input('\033[32m' + string + ' >> \033[0m')

    elif withConfirm:
        print('\033[31mDjango Console: ' + string + '\033[0m')
        while True:
            answer = input('\033[32m' + "Please respond with yes or no [Y/N/y/n]" + ' >> \033[0m').lower()
            if answer in [ "y", "Y", "yes", "Yes", "YES", "Yeah"]:
                return True
            elif answer in [ "n", "N", "no", "No", "NO", "Nope"]:
                return False        
    else:
        print('\033[32mDjango Coneole: \033[0m' + string)



def raise_error_message(func):

    try:
        errored_func = func.__name__
    except:
        errored_func = "Failed to get func information!"

    try:
        errored_obj  = str(func)
    except:
        errored_obj  = "Failed to get errored object information!"

    try:
        func_sig     = inspect.signature(func)
    except:
        func_sig     = "Failed to get functino signature!"


    return textwrap.dedent("""
Python Information:

Excute func name : {func_name}
Object Info      : {obj_inf}
Signature        : {func_signature}
    """).format(
        func_name = errored_func,
        obj_inf   = errored_obj,
        func_signature = func_sig
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
