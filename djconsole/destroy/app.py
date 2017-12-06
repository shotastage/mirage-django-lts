import shutil
from os import path
import tarfile

from djconsole.command import log
from djconsole.backup import backup


def _check(name):
    if path.isdir(name):
        return
    else:
        raise FileNotFoundError


def _backup(name):
    try:
        _check(name)
    except:
        return

    backup.create_buckup_dir()

    shutil.make_archive(name, "zip")

    shutil.move(name + ".zip", ".djc/backup/")
   
def _destroy(name):
    shutil.rmtree(name)
