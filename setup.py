from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "django-console=django-console.__main__:main"
        ]
    },
)
