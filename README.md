# Django Console
[![Build Status](https://travis-ci.org/shotastage/django-console.svg?branch=master)](https://travis-ci.org/shotastage/django-console)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Extended django admin or manage.py command.


# Usage

### Create a new Django project

If you excute this command without name, the interactive shell ask you a name of project.

```
djc new [NAME]
```

### Create Apps

You can create multiple Django apps at once.

```
djc generate app mail post api
```

And shorten command is here.

```
djc g app mail post api
```

### Create Model

You can create Django model class simply running one command.

```
djc g model Person name:string age:integer bio:text
```

If you want to have arguments,

```
djc g model TestModel uuid:string+autolen:maxlen=30,primary script:string+autolen:maxlen=400
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
djc s
```

or

```
djc server
```

### Run Interactive Shell

You can launch Python interactive shell like Rails console.

```
djc console
```

or

```
djc c
```

If you want to enter in database console, 

```
djc dbconsole
```

or

```
djc c:db
```


### Database Commands
Migrate database

```
djc db:migrate
```

### Run destroy app

You can delete Django app from your project.

```
djc destroy app [APP NAME]
```


# Requirements

- Python3

# Build & Install

```
pip install djconsole
```
# Author

- Shota Shimazu
