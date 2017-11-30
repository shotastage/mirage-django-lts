from os import getcwd, chdir
from contextlib import contextmanager


@contextmanager
def chdir(next):
    current = getcwd()
    chdir(next)
    yield
    chdir(current)
