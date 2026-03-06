[ wger project ](https://wger.readthedocs.io/en/latest/index.html)
latest  stable  2.4  2.0  1.9
Manual
  * [Using the routines](https://wger.readthedocs.io/en/latest/manual/routines.html)


Installation (prod)
  * [Docker compose](https://wger.readthedocs.io/en/latest/production/docker.html)
  * [](https://wger.readthedocs.io/en/latest/production/installation.html)
    * [wger user](https://wger.readthedocs.io/en/latest/production/installation.html#wger-user)
    * [Webserver](https://wger.readthedocs.io/en/latest/production/installation.html#webserver)
    * [Database](https://wger.readthedocs.io/en/latest/production/installation.html#database)
    * [Application](https://wger.readthedocs.io/en/latest/production/installation.html#application)
    * [Email](https://wger.readthedocs.io/en/latest/production/installation.html#email)
    * [Site Settings](https://wger.readthedocs.io/en/latest/production/installation.html#site-settings)
    * [Other changes](https://wger.readthedocs.io/en/latest/production/installation.html#other-changes)


Development
  * [Backend](https://wger.readthedocs.io/en/latest/development/backend.html)
  * [Frontend](https://wger.readthedocs.io/en/latest/development/frontend.html)
  * [Mobile App](https://wger.readthedocs.io/en/latest/development/mobile_app.html)


Administration
  * [Commands](https://wger.readthedocs.io/en/latest/administration/commands.html)
  * [Settings](https://wger.readthedocs.io/en/latest/administration/settings.html)
  * [Authentication Proxy (SSO)](https://wger.readthedocs.io/en/latest/administration/auth_proxy.html)
  * [Gym administration](https://wger.readthedocs.io/en/latest/administration/gym.html)


API
  * [Using the API](https://wger.readthedocs.io/en/latest/api/api.html)
  * [Using the routine API](https://wger.readthedocs.io/en/latest/api/routines.html)


All the rest
  * [Contributing](https://wger.readthedocs.io/en/latest/contributing.html)
  * [Changelog](https://wger.readthedocs.io/en/latest/changelog.html)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * Manual installation
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/production/installation.rst)


* * *
# Manual installation[](https://wger.readthedocs.io/en/latest/production/installation.html#manual-installation "Link to this heading")
Install `npm` / `nodejs` >= 22, and `sass`
If you plan to use video files, it’s recommended you install ffmpeg as well (this is not strictly necessary, it’s just used for better upload validation as well as the extraction of some information from the video files such as resolution, codec, etc):
```
apt-get install ffmpeg
pip install ffmpeg-python

```

## wger user[](https://wger.readthedocs.io/en/latest/production/installation.html#wger-user "Link to this heading")
It is recommended to add a dedicated user for the application:
```
sudo adduser wger --disabled-password --gecos ""

```

The following steps assume you did, but it is not necessary (nor is it necessary to call it ‘wger’). In that case, change the paths as needed.
## Webserver[](https://wger.readthedocs.io/en/latest/production/installation.html#webserver "Link to this heading")
**Apache**
Install apache and the WSGI module:
```
sudo apt-get install apache2 libapache2-mod-wsgi-py3
sudo vim /etc/apache2/sites-available/wger.conf

```

Configure apache to serve the application:
```
<Directory /home/wger/src>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>


<VirtualHost *:80>
    WSGIApplicationGroup %{GLOBAL}
    WSGIDaemonProcess wger python-path=/home/wger/src python-home=/home/wger/venv
    WSGIProcessGroup wger
    WSGIScriptAlias / /home/wger/src/wger/wsgi.py
    WSGIPassAuthorization On

    Alias /static/ /home/wger/static/
    <Directory /home/wger/static>
        Require all granted
    </Directory>

    Alias /media/ /home/wger/media/
    <Directory /home/wger/media>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/wger-error.log
    CustomLog ${APACHE_LOG_DIR}/wger-access.log combined
</VirtualHost>

```

Apache has a problem when uploading files that have non-ASCII characters, e.g. for exercise images. To avoid this, add to /etc/apache2/envvars (if there is already an `export LANG`, replace it) or set your system’s locale:
```
export LANG='en_US.UTF-8'
export LC_ALL='en_US.UTF-8'

```

Activate the settings and disable apache’s default:
```
sudo a2dissite 000-default.conf
sudo a2ensite wger
sudo service apache2 reload

```

**Alternatives**
You don’t _need_ to use apache, you can also use nginx, caddy or some other web server. Just set them up as a reverse proxy to a WSGI application server, and serve the static and media files:
<https://docs.djangoproject.com/en/dev/howto/deployment/>
Here’s an example with Caddy:
```
# /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=apache
Group=apache
WorkingDirectory=/var/www/wger/src
ExecStart=/var/www/wger/venv/bin/gunicorn --access-logfile - --workers 3 wger.wsgi:application -b :8000

[Install]
WantedBy=multi-user.target

```

```
# /etc/caddy/Caddyfile

your-domain {
    reverse_proxy localhost:8000

    handle_path /static/* {
        file_server {
            root "/var/www/wger/static"
        }
    }

    handle_path /media/* {
        file_server {
            root "/var/www/wger/media"
        }
   }
}

```

## Database[](https://wger.readthedocs.io/en/latest/production/installation.html#database "Link to this heading")
**PostgreSQL**
Install the Postgres server (choose the appropriate and currently supported version for your distro) and create a database and a user:
```
sudo apt-get install postgresql postgresql-server-dev-12 python3-psycopg2
sudo su - postgres
createdb wger
psql wger -c "CREATE USER wger WITH PASSWORD 'wger'";
psql wger -c "GRANT ALL PRIVILEGES ON DATABASE wger to wger";

```

You might want or need to edit your `pg_hba.conf` file to allow local socket connections or similar.
**SQLite**
If using sqlite, create a folder for it (must be writable by the apache user):
```
mkdir /home/wger/db
touch /home/wger/db/database.sqlite
chown :www-data -R /home/wger/db
chmod g+w /home/wger/db /home/wger/db/database.sqlite

```

## Application[](https://wger.readthedocs.io/en/latest/production/installation.html#application "Link to this heading")
As the wger user, make a virtualenv for python and activate it:
```
python3 -m venv /home/wger/venv
source /home/wger/venv/bin/activate

```

Create folders to collect all static resources and save uploaded files. The `static` folder will only contain CSS and JS files, so it must be readable by the apache process while `media` will contain the uploaded files and must be writeable as well:
```
mkdir /home/wger/{static,media}
chmod o+w /home/wger/media

```

Get the application:
```
git clone https://github.com/wger-project/wger.git /home/wger/src
cd /home/wger/src
pip install .

```

Set the python path so that the settings file can be imported from anywhere:
```
export PYTHONPATH=/home/wger/src

```

You can configure the application by setting environmental variables. For a commented list, refer to
<https://github.com/wger-project/docker/blob/master/config/prod.env>
Some important ones are:
```
export DJANGO_SECRET_KEY='your-very-long-and-random-secret-key'
export TIME_ZONE='Europe/Berlin'
export MEDIA_ROOT='/home/wger/media'
export STATIC_ROOT='/home/wger/static'
export ALLOWED_HOSTS='example.com,www.example.com'

# Postgres
export DJANGO_DB_ENGINE='django.db.backends.postgresql'
export DJANGO_DB_NAME='wger'
export DJANGO_DB_USER='wger'
export DJANGO_DB_PASSWORD='wger'
export DJANGO_DB_HOST='localhost'
export DJANGO_DB_PORT='5432'

# Sqlite
export DJANGO_DB_ENGINE='django.db.backends.sqlite3'
export DJANGO_DB_NAME='/home/wger/db/database.sqlite'

```

Run the installation script, this will download some CSS and JS libraries and load all initial data:
```
wger bootstrap

```

Collect all static resources:
```
python manage.py collectstatic

```

Compile the translation (.po) files:
```
cd wger
django-admin compilemessages

```

The bootstrap command will also create a default administrator user (you probably want to change the password as soon as you log in):
  * **username** : admin
  * **password** : adminadmin


## Email[](https://wger.readthedocs.io/en/latest/production/installation.html#email "Link to this heading")
The application is configured to use Django’s console email backend by default, which causes messages intended to be sent via email to be written to `stdout`.
In order to use a real email server, another backend listed in [Django’s documentation](https://docs.djangoproject.com/en/dev/topics/email/#email-backends) can be configured instead. Parameters for the backend are set as variables in `settings.py`. For example, the following allows an SMTP server at `smtp.example.com` to be used:
```
export ENABLE_EMAIL = True
export EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
export EMAIL_HOST = 'smtp.example.com'
export EMAIL_PORT = 587
export EMAIL_HOST_USER = 'wger@example.com'
export EMAIL_HOST_PASSWORD = 'example_password'
export EMAIL_USE_TLS = True
export EMAIL_USE_SSL = False
export FROM_EMAIL = 'wger Workout Manager <wger@example.com>'

```

Django provides a `sendtestemail` command via `manage.py` to test email settings:
```
python manage.py sendtestemail user@example.com

```

## Site Settings[](https://wger.readthedocs.io/en/latest/production/installation.html#site-settings "Link to this heading")
Some wger features make use of Django’s site name and domain settings in the `contrib.sites` framework. These should be set through the Python shell:
```
python manage.py shell
>>> from django.contrib.sites.models import Site
>>> site = Site.objects.get(pk=1)
>>> site.domain = 'wger.example.com'
>>> site.name = 'example.com wger Workout Manager'
>>> site.save()

```

where `wger.example.com` is the domain of the wger instance. This assumes that wger is using the default site ID of 1. If a different site ID is being used, it must be specified in `settings.py`:
```
SITE_ID = 2

```

## Other changes[](https://wger.readthedocs.io/en/latest/production/installation.html#other-changes "Link to this heading")
  * For a description of the available settings consult [Settings](https://wger.readthedocs.io/en/latest/administration/settings.html#settings).
  * If you want to use the application as a public instance, you will probably want to change the following templates:
    * **tos.html** , for your own Terms Of Service here
    * **about.html** , for your contact address or other such legal requirements
  * To keep the application updated, regularly pull new changes and
    * install new or updated dependencies: `pip install .`
    * apply new migrations: `python manage.py migrate --all`
    * update the static files: `npm install`, `npm run build:css:sass` and `python manage.py collectstatic`
    * update data `python3 manage.py sync-exercises`, `python3 manage.py download-exercise-images` (something like weekly) and `python3 manage.py sync-ingredients` (monthly)


[](https://wger.readthedocs.io/en/latest/production/docker.html "Docker compose") [Next ](https://wger.readthedocs.io/en/latest/development/backend.html "Backend")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**Augment Code Review** Outperforms Cursor by 20% on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
