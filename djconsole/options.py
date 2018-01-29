from enum import Enum

class DjConsoleOptions(Enum):
    # Create new django application
    dj_new = 1

    # Generate app, model, template, view and so on
    dj_gen = 2

    # Remove app or mtvs
    dj_destory = 3

    # Run Debug Server
    dj_server = 4


class DjGen(Enum):
    app = 1
    model = 2
    template = 3
    view = 4
