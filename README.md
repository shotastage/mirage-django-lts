# Django Console

Extended django admin or manage.py command.


# Usage

### Create a new Django project

If you excute this command without name, the interactive shell ask you a name of project.

```
djc new [NAME]
```

### Create Django apps

You can create multiple Django apps at once.

```
djc generate mail post api
```

And shorten command is here.

```
djc g mail post api
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
