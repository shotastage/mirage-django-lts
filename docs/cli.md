# Command Line Interface

- `new [project name (optional)]`


Create a new Django project. Running “new” will create Django project and front-end application template at once.

- `new:api`


Create a new Django REST API project. Running new:api will run pipenv install django-rest-framework internally and install rest framework to Django project automatically.

- `new:cms`

Create a new Django CMS project. Running new:cms will run pipenv install django-cms internally and install CMS framework to Django project automatically.


- `backup app [app name]` `b`


Running backup command will save Django app source tree as archive file. 
Saved archive will exist in project directory so if you remove project, backup file will be lost.



- `configure` `conf`

Running configure command will recreate DjFile interactively. If you run this command, old settings written in DjFile will be discarded. Thus, I recommend you to backup DjFile before reconfigure it.


- `console` `c`

Launch Django python shell to manage or test Django project directory.


- `console:db` `c:db`

Launch database console.


## Rest registred commands

```
 # Usage & Version
    parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", "version", None, "VersionShow")

    parser.add_argument("d", "destroy", "app", "DjangoDestroy")

    parser.add_argument_with_subaction("db", "database", "migrate", None, "DjangoMigrate")
    parser.add_argument_with_subaction("db", "database", "reset", None, "DjangoDBReset")

    # parser.add_argument("d", "destroy", None, "DjangoDestroy")

    parser.add_argument("g", "generate", "app", "DjangoAppMake")

    parser.add_argument("ide", "scaffold", None, "Scaffold")
    parser.add_argument("internal_server_launch", "internal_server_launch", None, "ScaffoldServer")

    parser.add_argument("s", "server", None, "DjangoDebugServer")

```
