from djconsole.command import log
from os import system

def launch_server():
    log("Runnng server...")

    try:
        system("python manage.py runserver")
    except KeyboardInterrupt:
        log("Good bye!")
