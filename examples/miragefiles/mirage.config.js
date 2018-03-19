version = "v0.0.4"

project = {
    "name": "Sample Project",
    "version": "0.0.1",
    "author": "Shota Shimazu",
    "email": "hornet.live.mf@gmail.com",
    "git": "https://github.com/shotastage/django-console.git",
    "license": "restricted",
    "description": "This is template!",

    django: {
        "path": "sample",
        "module": "sample",
        "package": "pipenv",
        "database": "PostgreSQL"
    },

    frontend: {
        "path": "shell",
        "package": "yarn",
        "builder": "webpack"
    },

    workspace: {
        "path": ".mirage"
    }
};

    
copyright = {
    "start_year": 2017,
    "copyrightors": [
        "Shota Shimazu",
        "Aika Yamashita"
    ]
};