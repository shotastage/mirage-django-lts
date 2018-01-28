import sys

def in_project():
    try:
        sys.path.append("./")
        import manage

        return True
    except:
        return False
