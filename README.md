# Mirage
[![Build Status](https://travis-ci.org/shotastage/mirage.svg?branch=master)](https://travis-ci.org/shotastage/mirage)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Extended django admin or manage.py command.


# Usage

### Create a new Django project

If you excute this command without name, the interactive shell ask you a name of project.

```
mg new [NAME]
```

### Create Apps

You can create multiple Django apps at once.

```
mg generate app mail post api
```

And shorten command is here.

```
mg g app mail post api
```

### Create Model

You can create Django model class simply running one command.

```
mg g model Person name:string age:integer bio:text
```

If you want to have arguments,

```
mg g model TestModel uuid:string+autolen:maxlen=30,primary script:string+autolen:maxlen=400
```

Created model class is here.

```:python
class TestModel(models.Model):
    uuid = models.CharField(max_length=30, primary_key=True)
    script = models.CharField(max_length=400)

```

### Run debug server

Run Django debug server like `rails s`.

```
mg s
```

or

```
mg server
```

### Run Interactive Shell

You can launch Python interactive shell.

```
mg console
```

or

```
mg c
```

If you want to enter in database console, 

```
mg c:db
```


### Database Commands
Migrate database

```
mg db:migrate
```

Reset database

```
mg db:reset
```

### Run destroy app

You can delete Django app from your project.

```
mg destroy app [APP NAME]
```


# Requirements

- Python3

# Build & Install

```
make before_all
make build_all
```
# Author

- Shota Shimazu
