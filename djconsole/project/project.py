import sys

def in_project():
    try:
        set_import_root()

        import manage

        return True
    except ImportError:
        return False

def in_app():
    set_import_root()

def set_import_root():
    sys.path.append("./")
