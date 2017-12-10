#!/usr/bin/env python

from os import system
from sys import argv

if __name__ == "__main__":
    args = argv

    try:
        opt = args[1]
    except:
        opt = "none"

    system("python setup.py check")
    system("python setup.py sdist")

    if opt == "--update":
        system("pip uninstall djconsole")

    system("pip install dist/djconsole-0.0.8.tar.gz")
