import textwrap

def create_urlpy_script(app):

    django_version = "no_version"

    return textwrap.dedent(
'''
from django.conf.urls import url
from {app}.views import """YOUR_VIEW_CLASS"""

urlpatterns = [
    url(r'^url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]

''').format(app=app).strip()
