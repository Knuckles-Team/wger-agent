[ wger project ](https://wger.readthedocs.io/en/latest/index.html)
latest  stable  2.4  2.0  1.9
Manual
  * [Using the routines](https://wger.readthedocs.io/en/latest/manual/routines.html)


Installation (prod)
  * [Docker compose](https://wger.readthedocs.io/en/latest/production/docker.html)
  * [Manual installation](https://wger.readthedocs.io/en/latest/production/installation.html)


Development
  * [Backend](https://wger.readthedocs.io/en/latest/development/backend.html)
  * [Frontend](https://wger.readthedocs.io/en/latest/development/frontend.html)
  * [Mobile App](https://wger.readthedocs.io/en/latest/development/mobile_app.html)


Administration
  * [](https://wger.readthedocs.io/en/latest/administration/commands.html)
    * [Administration Commands](https://wger.readthedocs.io/en/latest/administration/commands.html#administration-commands)
    * [Management commands](https://wger.readthedocs.io/en/latest/administration/commands.html#management-commands)
    * [Celery](https://wger.readthedocs.io/en/latest/administration/commands.html#celery)
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
  * Commands
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/administration/commands.rst)


* * *
# Commands[](https://wger.readthedocs.io/en/latest/administration/commands.html#commands "Link to this heading")
Please note that the administration commands are intended e.g. to bootstrap/install an application to a new system, while the management ones are made to administer a running application (to e.g. delete guest users, send emails, etc.).
## Administration Commands[](https://wger.readthedocs.io/en/latest/administration/commands.html#administration-commands "Link to this heading")
Use the `wger` command to perform different administration and bootstrapping tasks such as initialising the database. You can get a list of all available commands by calling `wger` without any arguments as well as help on a specific command with `wger --help <command>`.
Here are some of the most important ones:

`bootstrap`

This command bootstraps the application: it creates a settings file, initialises a SQLite database, loads all necessary fixtures for the application to work and creates a default administrator user. While it can also work with e.g. a PostgreSQL database, you will need to create it yourself:

`create-or-reset-admin`

Makes sure that the default administrator user exists. If you change the password, it is reset.

`load-fixtures`

loads all fixture files with the default data. This data includes all data necessary for the application to work such as: * exercises, muscles, equipment * ingredients, units * languages * permission groups * etc.
Note that ingredients are not included and need to be installed separately with download-online-fixtures.

`load-online-fixtures`

Downloads a subset of ingredients, the weight units fixtures and installs them. If you want to download all ingredients, you need to use the manage.py command with the `sync-ingredients` (see below).
Downloads a subset of ingredients and the weight units fixtures, then installs them. To download all ingredients, use the manage.py command with the `sync-ingredients` option (see below).

`import-off-products`

Imports and updates products from the Open Food Facts database. You can select whether to use a local file with the full database dump, the daily delta updates or use a mongo database, see the help for more information.
## Management commands[](https://wger.readthedocs.io/en/latest/administration/commands.html#management-commands "Link to this heading")
wger also implements a series of Django commands that perform different management functions that are sometimes needed. Call them with `python manage.py <command_name>`.
To retrieve a full list of available commands, call `python manage.py` without any arguments and look under the app names (weight, nutrition, manager, core, exercises). To get help on a specific command, call `python manage.py <command_name> --help`.
Here are some of the most important ones:

`sync-ingredients[-async]`

synchronizes the ingredient database from the default wger instance to the local installation. Ingredients that you added manually to the database are not touched. The `async` version uses celery to perform the task in the background. Also note that this will use around 1GB of disk space and takes several hours to complete.

`sync-exercises`

synchronizes the exercise database from the default wger instance to the local installation. This will also update categories, equipment, languages, muscles and will delete entries that were removed on the remote server (this basically only applies to exercises that were submitted several times). Exercises that you added manually to the database are not touched.

`download-exercise-images`

synchronizes the exercise images from the default wger instance to the local installation, does not overwrite existing images.

`download-exercise-videos`

synchronizes the exercise videos from the default wger instance to the local installation, does not overwrite existing videos.

`exercises-health-check.py`

Performs a series of basic health checks. Basically sees if there are exercises that don’t have a default English translation or worse, don’t have any translation at all

`extract-i18n`

Used for development only. Extracts strings from the database that need to be translated. See the [Internationalization (i18n)](https://wger.readthedocs.io/en/latest/development/i18n.html#i18n) section for more information.

`dummy-generator-*`

Use to generate dummy data for the different entry types. For more information see the [Dummy data generator](https://wger.readthedocs.io/en/latest/development/others.html#dummy-generator) section.
## Celery[](https://wger.readthedocs.io/en/latest/administration/commands.html#celery "Link to this heading")
To list the currently scheduled tasks:
```
celery -A wger inspect active

```

To to clear the currently waiting tasks:
```
from wger.celery_configuration import app
app.control.purge()

```

For other possible commands, consult the [celery documentation](https://docs.celeryq.dev/en/latest/reference/celery.app.control.html).
[](https://wger.readthedocs.io/en/latest/development/mobile_app.html "Mobile App") [Next ](https://wger.readthedocs.io/en/latest/administration/settings.html "Settings")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
