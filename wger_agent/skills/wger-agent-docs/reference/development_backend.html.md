[ wger project ](https://wger.readthedocs.io/en/latest/index.html)
latest  stable  2.4  2.0  1.9
Manual
  * [Using the routines](https://wger.readthedocs.io/en/latest/manual/routines.html)


Installation (prod)
  * [Docker compose](https://wger.readthedocs.io/en/latest/production/docker.html)
  * [Manual installation](https://wger.readthedocs.io/en/latest/production/installation.html)


Development
  * [](https://wger.readthedocs.io/en/latest/development/backend.html)
    * [Development with docker](https://wger.readthedocs.io/en/latest/development/backend.html#development-with-docker)
    * [Local installation](https://wger.readthedocs.io/en/latest/development/backend.html#local-installation)
    * [And now](https://wger.readthedocs.io/en/latest/development/backend.html#and-now)
    * [Release process](https://wger.readthedocs.io/en/latest/development/backend.html#release-process)
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
  * Backend
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/development/backend.rst)


* * *
# Backend[](https://wger.readthedocs.io/en/latest/development/backend.html#backend "Link to this heading")
The backend is a Django application, the repository can be found at:
<https://github.com/wger-project/wger>
## Development with docker[](https://wger.readthedocs.io/en/latest/development/backend.html#development-with-docker "Link to this heading")
[Development with docker](https://wger.readthedocs.io/en/latest/development/docker.html#development-docker) provides a quick way to setup a development environment
## Local installation[](https://wger.readthedocs.io/en/latest/development/backend.html#local-installation "Link to this heading")
Install `npm`, `sass` and, optionally, [uv](https://docs.astral.sh/uv/)
Download the source code:
```
git clone https://github.com/wger-project/wger.git server
cd server

```

If using `uv`:
```
uv sync
uv pip install -e .
source .venv/bin/activate

```

Otherwise, manually create a new virtualenv and install everything:
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install --group dev .
pip install -e .

```

This will download the required JS and CSS libraries and create an SQLite database and populate it with data on the first run:
```
export DJANGO_SETTINGS_MODULE=settings.local_dev
export PYTHONPATH=/path/to/wger/server
wger bootstrap
wger load-online-fixtures

```

It’s recommended to make a backup of the SQLite database after the initial bootstrap, just copy it to some other place:
```
cp database.sqlite database.sqlite.orig

```

You can of course also use other databases such as PostgreSQL or MariaDB. Create a database and user and edit the DATABASES settings before calling bootstrap. Take a look at the prod_postgres on apache on how that could look like.
Compile the translation files:
```
cd wger
django-admin compilemessages

```

After all this you can just use Django’s development server:
```
$ python manage.py runserver

```

That’s it. You can log in with the default administrator user:
  * **username** : admin
  * **password** : adminadmin


You can reset the admin’s password with `wger create-or-reset-admin`.
## And now[](https://wger.readthedocs.io/en/latest/development/backend.html#and-now "Link to this heading")
  * For a description of the available settings consult [Settings](https://wger.readthedocs.io/en/latest/administration/settings.html#settings).
  * You might need to start [Celery](https://wger.readthedocs.io/en/latest/development/celery.html#celery) as well if you want to to run certain commands in the background.
  * For managing i18n files consult [Internationalization (i18n)](https://wger.readthedocs.io/en/latest/development/i18n.html#i18n).
  * Check the [Dummy data generator](https://wger.readthedocs.io/en/latest/development/others.html#dummy-generator) for generating dummy data.
  * Take a look at django extensions, a collection of custom extensions and commands:
<https://django-extensions.readthedocs.io/>
E.g. you can use `runserver_plus` instead of the default Django server as you can use an interactive debugger directly from the browser if an exception occurs. It also accepts the same command-line options. For this just install the following packages:
```
pip install django_extensions werkzeug
python manage.py runserver_plus [options]

```



## Release process[](https://wger.readthedocs.io/en/latest/development/backend.html#release-process "Link to this heading")
Before releasing a new (major or minor) version of the backend, a couple of manual steps are still necessary.
Yes, some of these steps could and should be automated, but for now they are not. This might also be one of the reasons why there are not that many releases…
  1. Bump version


Bump the version in:
  * `wger/version.py`
  * `package.json` (not really needed, but since it’s there, let’s keep it up to date)
  * All the `.github/workflows/docker-*.yml` files
  * `docs/conf.py` (in the docs repo)


  1. Update contributors list


Run the script that updates the contributors list:
```
python3 extras/authors/generate_authors_api.py

```

  1. Update exercise fixture


It’s recommended to update the exercise fixture before a release. To do this extract them from a current database, split the files and and copy them as appropriate:
```
python ./manage.py dumpdata --indent 4 --natural-foreign exercises > extras/scripts/data.json
cd extras/scripts/
python3 filter-fixtures.py
cp categories.json ../../wger/exercises/fixtures/

```

  1. Update translations


Update the po files as described in [Internationalization (i18n)](https://wger.readthedocs.io/en/latest/development/i18n.html#i18n).
  1. Tag the release


Create a new tag for the release:
```
git tag -a 1.2.3 -m "Release 1.2.3"
git push origin 1.2.3

```

  1. Create a new release on GitHub


Finally, create a new release on GitHub from the tag. Generate the description from the pull requests and edit if necessary. Copy this changelog to the docs repo and add it to the existing changelog.rst.
  1. Talk about it!


Write an announcement, and post it on discord, mastodon, etc.
[](https://wger.readthedocs.io/en/latest/production/installation.html "Manual installation") [Next ](https://wger.readthedocs.io/en/latest/development/frontend.html "Frontend")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**Augment Code Review** Outperforms Cursor by 20% on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
