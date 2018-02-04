import textwrap

def make_procfile():
    return '''
web: gunicorn pinna.wsgi
    '''

def make_runtime():
    return '''
python-3.6.0
    '''
