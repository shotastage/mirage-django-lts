from djconsole.command import log
from os import system

def launch_server():
    log("Runnng server...")
    system("python manage.py runserver")
