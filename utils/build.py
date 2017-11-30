#!/usr/bin/env python

from os import system

if __name__ == "__main__":
    system("python setup.py check")
    system("python setup.py sdist")

    system("pip uninstall djconsole")
    system("pip install dist/djconsole-0.0.1.tar.gz")
