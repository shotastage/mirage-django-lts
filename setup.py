# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./mirage')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "django-mirage",
        version = "0.0.17",
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        classifiers=[
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
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
                'djc = mirage.mirage:main',
                'mg = mirage.mirage:main',
                'mi = mirage.mirage:main'
            ],
        },
        description = "Advanced Django console",
        long_description = "Advanced extended command line tool for Django.",
        url = "https://github.com/shotastage/django-mirage/",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "mirage_test.suite",
    )
