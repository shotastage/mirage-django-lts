# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./mirage')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "django-mirage",
        version = "0.0.23",
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        packages = find_packages(exclude=('tests', 'shell')),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            "Flask"
        ],
        entry_points = {
            'console_scripts':[
                'djc = mirage.mirage:main',  # Recent command
                'mirage = mirage.mirage:main',
                'mg = mirage.mirage:main'
            ],
        },
        description = "Advanced Django Console",
        long_description = "Advanced extended command line tool for Django.",
        url = "https://github.com/shotastage/django-mirage/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "mirage_test.suite",
    )
