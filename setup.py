# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name = "djconsole",
        version='0.0.2',
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        packages = find_packages(),
        install_requires=[
            "django",
        ],
        entry_points = {
            'console_scripts':[
                'djc = djconsole.djconsole:main',
            ],
        },
        description = "Advanced Django console",
        long_description = "Advanced Django command line tools like Rails.",
        url = "https://github.com/shotastage/django-console/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
    )
