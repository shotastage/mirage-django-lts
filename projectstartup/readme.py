import textwrap

def create_readme_doc(name):

    django_version = "no_version"

    return textwrap.dedent(
'''
# {name}
This is your first Django application.

# Info

## Django Version
{django_version}

''').format(name=name, django_version=django_version).strip()
