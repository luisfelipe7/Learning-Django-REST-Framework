<h1 align="center">
  <br>
  <a href="https://github.com/luisfelipe7/Learning-Django-REST-Framework.git"><img src="https://rawgit.com/luisfelipe7/Learning-Django-REST-Framework/master/django.png" alt="Markdownify" width="430"></a>
   <a href="https://github.com/luisfelipe7/Learning-Django-REST-Framework.git"><img src="https://rawgit.com/luisfelipe7/Learning-Django-REST-Framework/master/postgresql.png" alt="Markdownify" width="200"></a>
  <br>
  Learning-Django-REST-Framework
  <br>
</h1>
<h4 align="center">Creating a Django project with the tutorial given on the official website of  <a href="http://www.django-rest-framework.org/" target="_blank">Django-REST-Framework</a>.</h4>

<p align="center">
  •<a href="#key-features">&nbsp; Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#run-it">Run it</a> •
  <a href="#how-to-use-it">How to use it</a> •
  <a href="#extras">Extras</a> •
  <a href="#credits">Credits</a>
</p>

## Key Features
Basic aspects about Django REST Framework:
* Serialization.
* Requests & Responses.
* Class-based views.
* Authentication & permissions.
* Relationships & hyperlinked APIs.
* Viewsets & routers.
* Schemas & client libraries.


## Installation

1. Donwload Python 3 from https://www.python.org/downloads/.
2. Install Pip with this link: https://pip.pypa.io/en/stable/installing/ , if you
   don't know if you have pip, type this command
```bash
# Verify pip
$ pip -V
```
   Once you have pip installed, update pip with this command
```bash
# Update pip
$ pip install -U pip
```    
3.  Download or clone this repository in your folder
```bash
# Clone this repository
$ git clone https://github.com/luisfelipe7/Learning-Django-REST-Framework
```
4. Go into the repository
```bash
# Go into the repository
$ cd Learning-Django-REST-Framework
```

5. Create a virtual environment
```bash
# Install virtualenv 
$ sudo pip install virtualenv 
```
```bash
# Create a virtual environment with Python3, env is the name of the environment
$ virtualenv env --python=python3 
```
```bash
# Activate your environment
$ cd env
$ source bin/activate 
```
 6. With the activated environment, install the requirements:
 ```bash
# Install requirements
$ pip install -r requirements.txt
```
  7. Run it.

## Run it
1. Install Postgresql
```bash
# Install postgresql
$ sudo apt-get install postgresql
```
2. Connecting to PostgreSQL for first time <br><br>
a) Run the psql command from the postgres user account
```bash
# Enter with the user postgres
$ sudo -u postgres psql postgres
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Set the password
```bash
# Enter this command for set the password
$ \password postgres
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c) Enter a password <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d) Close psql
```bash
# Close psql
$ \q
```
3. Create a new user and database <br><br>
a) Enter to Postgresql
```bash
# Enter with the user postgres
$ su - postgres  
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b) Create the new user and database
```bash
postgres=# CREATE USER admin WITH PASSWORD 'admin';
postgres=# CREATE DATABASE mydatabase OWNER admin;
```
4. Configure your database, paste in settings.py file of your Django project the next configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
5. Allow local connections, edit the file pg_hba.conf (/etc/postgresql/9.6/main/pg_hba.conf) as a superuser and replace the final lines of the file with these lines:
```
# Database administrative login by Unix domain socket
local   all             postgres                                md5

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
# Allow replication connections from localhost, by a user with the
# replication privilege.
#local   replication     postgres                                peer
#host    replication     postgres        127.0.0.1/32            md5
#host    replication     postgres        ::1/128                 md5
```
If you want to allow remote connections, visit this link:
http://suite.opengeo.org/opengeo-docs/dataadmin/pgGettingStarted/firstconnect.html

6. Sync your models
```bash
# Apply Migrations
$ python manage.py migrate
```
7. Create a superuser for admin views
```bash
# Create a superuser
$ python manage.py createsuperuser
```
8. Run your development server
```bash
# Run a development server
$ python manage.py runserver
```

## How to use it

Enter to these URL's:
* http://127.0.0.1:8000/snippets/
* http://127.0.0.1:8000/snippets/2

## Extras

How to install and use Pgadmin :
1. First, Pgadmin require Flask, so we need to install it with pip:
```bash
# Install flask
$ pip install flask
```
2. Donwload the Pgadmin from the next url (<b> I don't recommend download the last version, because it have some bugs </b>) :
				https://www.postgresql.org/ftp/pgadmin/pgadmin4/
3. According to the dowloaded file, install it with the next command:
 
```bash
# Install Pgadmin
$ pip install pgadmin4-3.2-py2.py3-none-any.whl
```
4. For run it use this command:
```bash
# Python Version - pgAdmin4.py file
$ sudo python3.5  "/home/felipe/Escritorio/Solvo/Documentacion Tecnica/Proyectos/Entornos Virtuales/env2/lib/python3.5/site-packages/pgadmin4/pgAdmin4.py"
```
5. Configure it, click on create server and follow these images:<br>

 <a href="https://github.com/luisfelipe7/Learning-Django-REST-Framework.git"><img src="https://rawgit.com/luisfelipe7/Learning-Django-REST-Framework/master/PgAdmin4-Config1.png" alt="Markdownify" width="430"></a>
  <a href="https://github.com/luisfelipe7/Learning-Django-REST-Framework.git"><img src="https://rawgit.com/luisfelipe7/Learning-Django-REST-Framework/master/PgAdmin4-Config2.png" alt="Markdownify" width="430"></a>

## Credits

Thanks to Django-REST-Framework for the tutorial given on the official website.

- [Django-REST-Framework](http://www.django-rest-framework.org/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

---

> GitHub [@luisfelipe7](https://github.com/luisfelipe7) &nbsp;&middot;&nbsp;
