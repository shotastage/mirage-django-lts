# Django Console

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


### Run debug server

Run Django debug derver like `rails s`.

```
djc s
```

or

```
djc server
```


# Requirements

- Python3

# Build & Install

```
./utils/build.py
```
# Author

- Shota Shimazu
