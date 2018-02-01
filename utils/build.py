#!/usr/bin/env python

import shutil


from os import system
from sys import argv


def build_assets():
    system("./shell/node_modules/.bin/node-sass ./shell/static/scss/main.scss ./shell/static/style/main.css")

def copy_static():
    try:
        shutil.copytree("shell/static/", "djconsole/scaffold/static/")
        shutil.copytree("shell/templates/", "djconsole/scaffold/templates/")
    except:
        print("Failed to copy statics.")



if __name__ == "__main__":
    args = argv

    try:
        opt = args[1]
    except:
        opt = "none"


    build_assets()
    copy_static()


    system("python setup.py check")
    system("python setup.py sdist")

    if opt == "--update":
        system("pip uninstall djconsole")

    system("pip install dist/djconsole-0.0.11.tar.gz")
