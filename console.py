

def log(string, withError = False, withInput = False):
    if withError:
        print('\033[31mDjango Console: ' + string + '\033[0m')
    elif withInput:
        return input('\033[32m' + string + ' >> \033[0m')
    else:
        print('\033[32mDjango Coneole: \033[0m' + string)
