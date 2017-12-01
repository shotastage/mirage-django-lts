import textwrap

def create_model_py(class_name, contents):

    django_version = "no_version"

    return textwrap.dedent(
'''
from django.db import models

# Create your models here.

class {class_name}(models.Model):
{contents}

''').format(class_name=class_name, contents=contents).strip()
