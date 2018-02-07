# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./djconsole')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "django-mirage",
        version = "0.0.11",
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        packages = find_packages(exclude=('tests', 'shell')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            "pipenv",
            "pyyaml",
            "Flask"
        ],
        entry_points = {
            'console_scripts':[
                'dj = mirage.mirage:main',
            ],
        },
        description = "Advanced Django console",
        long_description = "Advanced Django command line tools like Rails.",
        url = "https://github.com/shotastage/django-console/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "djconsole_test.suite",
    )
