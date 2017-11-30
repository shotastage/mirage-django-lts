# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name = "django-console",
    version = "0.0.1",
    author = "Shota Shimazu",
    author_email = "hornet.live.mf@gmail.com",
    packages = find_packages(),
    install_requires=[
        "django",
    ],
    description = "Advanced Django comsole",
    long_description = "Advanced Django command line tools like Rails.",
    url = "https://github.com/shotastage/django-console/",
    license = "Apache",
    platforms = ["POSIX", "Windows", "Mac OS X"],
    entry_points={
        'console_scripts': 'django = django-console:main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
    ]
)
