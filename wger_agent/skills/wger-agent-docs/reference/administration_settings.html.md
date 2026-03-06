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
  * Settings
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/administration/settings.rst)


* * *
# Settings[](https://wger.readthedocs.io/en/latest/administration/settings.html#settings "Link to this heading")
You can configure some of the application behaviour with the `WGER_SETTINGS` dictionary in your settings file. Currently, the following options are supported:

`ALLOW_GUEST_USERS`

Default `True`
Controls whether users can use the site as a guest user or if an administrator has to create the user accounts, as with the option above.

`ALLOW_REGISTRATION`

Default `True`
Controls whether users can register on their own or if a gym administrator has to create the user accounts.

`DOWNLOAD_INGREDIENTS_FROM`

Default `WGER`
Where to download ingredient images from. Set to ‘None’ to deactivate.

`EMAIL_FROM`

Default `wger Workout Manager <wger@example.com>`
The sender address used for sent emails by the system such as weight reminders

`EXERCISE_CACHE_TTL`

Default `3600` (one hour)
Sets how long the overview responses for exercise, exerciseinfo and exercisebaseinfo are cached for.

`INGREDIENT_CACHE_TTL`

Default `604800` (one week)
Sets how long the overview responses for ingredients are cached for.

`ROUTINE_CACHE_TTL`

Default `4 * 604800` (four weeks)
Sets how long the overview responses for routines are cached for.

`MIN_ACCOUNT_AGE_TO_TRUST`

Default `21`
Users won’t be able to contribute to exercises if their account age is lower than this amount in days.

`SYNC_EXERCISES_CELERY`

Default `False`
Whether to periodically synchronize the exercise database from the default wger instance. Needs celery to be configured.

`SYNC_EXERCISE_IMAGES_CELERY`

Default `False`
Whether to periodically synchronize the exercise images from the default wger instance. Needs celery to be configured.

`SYNC_EXERCISE_VIDEOS_CELERY`

Default `False`
Whether to periodically synchronize the exercise videos from the default wger instance. Needs celery to be configured.

`USE_CELERY`

Default `False`.
Whether celery is configured and can be used

`USE_RECAPTCHA`

Default `False`.
Controls whether a captcha challenge will be presented when new users register.

`WGER_INSTANCE`

Default `https://wger.de`.
The wger instance from which commands like exercise synchronization will use to fetch data from.
Note
If you want to override a default setting, don’t overwrite all the dictionary but only the keys you need, e.g. `WGER_SETTINGS['foo'] = 'bar'`. This avoids problems when new keys are added in the global settings.
[](https://wger.readthedocs.io/en/latest/administration/commands.html "Commands") [Next ](https://wger.readthedocs.io/en/latest/administration/auth_proxy.html "Authentication Proxy \(SSO\)")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
