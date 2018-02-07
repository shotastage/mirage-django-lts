import tempfile

def is_available_update():
    with tempfile.NamedTemporaryFile() as tmp:
        filename = tmp.name
