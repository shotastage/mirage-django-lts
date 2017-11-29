from subprocess import check_output, DEVNULL, STDOUT

def log(string, withError = False, withExitOnError = False, withInput = False):
    if withError:
        print('\033[31mDjango Console: ' + string + '\033[0m')

        if withExitOnError:
            exit(1)

    elif withInput:
        return input('\033[32m' + string + ' >> \033[0m')

    else:
        print('\033[32mDjango Coneole: \033[0m' + string)


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
