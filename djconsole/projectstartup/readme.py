import django
import textwrap

def create_readme_doc(name):

    return textwrap.dedent(
'''
# {name}

This is your first Django application.

# Info

## Django Version
{django_version}

''').format(name = name, django_version = get_django_version()).strip()


def get_django_version():
    version = django.VERSION
    return str(version[0]) + "." + str(version[1]) + "." + str(version[2])
