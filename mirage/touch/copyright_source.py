import textwrap

def copyright_doc(pr):
    return textwrap.dedent('''
{PROJECT_NAME}
{FILE_NAME}

Created by {YOUR_NAME} on {CURRENT_YEAR}

Copyright (c) {START_YEAR}-{CURRENT_YEAR} {COPYRIGHT_AUTHOR} All Rights Reserved.
Copyright (c) {START_YEAR}-{CURRENT_YEAR} {COPYRIGHT_AUTHOR} All Rights Reserved.

This software is released under the terms of {LICENSE_NAME}, see LICENSE for detail.
{LICENSE_URL}
    ''').format(
        PROJECT_NAME = name,
        FILE_NAME = get_os_name(),
        YOUR_NAME = get_django_version(),
        CURRENT_YEAR = get_python_version(),
        START_YEAR = get_pip_list(),
        COPYRIGHT_AUTHOR = "",
        LICENSE_NAME = "",
        LICENSE_URL = ""
    ).strip()
