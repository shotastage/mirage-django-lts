# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
from mirage.version import __version__ as ver
import sys


sys.path.append('./mirage')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "mirage-django-lts",
        version = ver,
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        packages = find_packages(exclude=('tests', 'shell')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            # "Flask"
        ],
        entry_points = {
            'console_scripts':[
                'mirage = mirage.mirage:main',
                'mg = mirage.mirage:main',
                'mgl = mirage.mirage:main',
            ],
        },
        description = "Advanced Django Console (LTS Version)",
        long_description = "Advanced extended command line tool for Django.",
        url = "https://github.com/shotastage/mirage-django-lts/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "mirage_test.suite",
    )
