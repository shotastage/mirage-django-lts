# Command Line Interface 

- `new [project name (optional)]`


Create a new Django project. Running “new” will create Django project and front-end application template at once.

- `new:api`


Create a new Django REST API project,. Running new:api will run pipenv install django-rest-framework internally and install rest framework to Django project automatically.


- `backup app [app name]` `b`


Running backup command will save Django app source tree as archive file. 
Saved archive will exist in project directory so if you remove project, backup file will be lost.



- `configure` `conf`

Running configure command will recreate DjFile interactively. If you run this command, old settings written in DjFile will be discarded. Thus, I recommend you to backup DjFile before reconfigure it.


- `console` `c`

Launch Django python shell to manage or test Django project directory.
