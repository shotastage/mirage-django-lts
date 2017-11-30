#!/usr/bin/env python

from os import system
from sys import argv

if __name__ == "__main__":
    args = argv

    system("python setup.py check")
    system("python setup.py sdist")

    if args[1] == "--update":
        system("pip uninstall djconsole")

    system("pip install dist/djconsole-0.0.1.tar.gz")
