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
  * [](https://wger.readthedocs.io/en/latest/api/api.html)
    * [Using the routine API](https://wger.readthedocs.io/en/latest/api/routines.html)
    * [JWT Tokens](https://wger.readthedocs.io/en/latest/api/api.html#jwt-tokens)
    * [Permanent Token](https://wger.readthedocs.io/en/latest/api/api.html#permanent-token)
    * [Pagination](https://wger.readthedocs.io/en/latest/api/api.html#pagination)
    * [Format negotiation](https://wger.readthedocs.io/en/latest/api/api.html#format-negotiation)
    * [Ordering](https://wger.readthedocs.io/en/latest/api/api.html#ordering)
    * [Filtering resources](https://wger.readthedocs.io/en/latest/api/api.html#filtering-resources)
  * [Using the routine API](https://wger.readthedocs.io/en/latest/api/routines.html)


All the rest
  * [Contributing](https://wger.readthedocs.io/en/latest/contributing.html)
  * [Changelog](https://wger.readthedocs.io/en/latest/changelog.html)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * Using the API
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/api/api.rst)


* * *
# Using the API[](https://wger.readthedocs.io/en/latest/api/api.html#using-the-api "Link to this heading")
Public endpoints, such as the list of exercises or the ingredients can be accessed without authentication. For user owned objects such as routines, you need to authenticate.
For some info on how to create routines over the API, see
  * [Using the routine API](https://wger.readthedocs.io/en/latest/api/routines.html)


## JWT Tokens[](https://wger.readthedocs.io/en/latest/api/api.html#jwt-tokens "Link to this heading")
This is the suggested way. You generate a temporary token which you send in the header with each request that needs authorization
  1. Get the tokens


Send your username and password to the `/api/v2/token` endpoint, you will get an `access` and a `refresh` token back:
```
result = requests.post(
    'https://wger.de/api/v2/token',
    data={'username': 'user', 'password': 'admin'}
)
access_token = result.json()['access']
refresh_token = result.json()['refresh']

print(result.json())
>>> {'refresh': 'eyJhbGciOiJIUzI1...', 'access': 'eyJhbGciOiJIUzI...'}

```

  1. Authenticate


Pass the access token in the Authorization header as `"Bearer: your-token"`:
```
result = requests.get(
    'https://wger.de/api/v2/workout/',
    headers={'Authorization': f'Bearer {access_token}'}
)

print(result.json())
>>> {'count': 5, 'next': None, 'previous': None, 'results': [{'id':.....

```

Additionally, you can send the access token to `/token/verify/` endpoint to verify it:
```
result = requests.post('https://wger.de/api/v2/token/verify', data={'token': access_token})

```

  1. Refresh


When this short-lived access token expires, you can use the longer-lived `refresh` token to obtain another access token:
```
result = requests.post(
    'https://wger.de/api/v2/token/refresh/',
    data={'refresh': refresh_token}
)
token = result.json()

print(token)
>>> {'access': 'eyJhbGciOiJI...'}

```

## Permanent Token[](https://wger.readthedocs.io/en/latest/api/api.html#permanent-token "Link to this heading")
You can also pass a permanent token in the header to authenticate, but this method should be considered deprecated:
```
token = 'abcdef123...'
result = requests.get(
    'https://wger.de/api/v2/routine/',
    headers={'Authorization': f'Token {token}'}
)

print(result.json())
>>> {'count': 5, 'next': None, 'previous': None, 'results': [{'id':.....

```

To generate a key, visit the API page on the web app.
You can also get a permanent token from the `login` endpoint. Send a username and password in a POST request. If the user doesn’t currently have a token, a new one will be generated for you
## Pagination[](https://wger.readthedocs.io/en/latest/api/api.html#pagination "Link to this heading")
By default all results are paginated by 20 elements per page. If you want to change this value, add a `?limit=<xxx>` to your query. You will find in the answer JSON the `next` and `previous` keywords with links to the next or previous result pages.
## Format negotiation[](https://wger.readthedocs.io/en/latest/api/api.html#format-negotiation "Link to this heading")
At the moment only JSON and the browsable HTML view are supported. That means that you can use the same endpoints from your browser or a client. Because of this, for the majority of REST clients it will not be necessary to explicitly set the format, but you have the following options:
  *

Set the **Accept** header:

    * `application/json`
    * `application/json; indent=4` - useful for debugging, will indent the result
    * `text/html` - browsable HTML view, like in the browser
  *

Set the format **directly in the URL** :

    * `/api/v2/<endpoint>.json/`
    * `/api/v2/<endpoint>/?format=json`
    * `/api/v2/<endpoint>.api/` - browsable HTML view


## Ordering[](https://wger.readthedocs.io/en/latest/api/api.html#ordering "Link to this heading")
Simply use `?ordering=<fieldname>` to order by that field. You can also specify more than one field name, just give it a list separated by commas `?ordering=<field1>,<field2>`. To reverse the order use like in django a `-` in front of the field.
## Filtering resources[](https://wger.readthedocs.io/en/latest/api/api.html#filtering-resources "Link to this heading")
You can easily filter all resources by specifying the filter queries in the URL: `?<fieldname>=<value>`, combinations are possible, the filters will be AND-joined: `<f1>=<v1>&<f2>=<v2>`. Please note that for boolean values you must pass ‘False’ or ‘True’ other values, e.g. 1, 0, false, etc. will be ignored. Like with not filtered queries, your objects will be available under the ‘results’ key.
Note that it is not currently possible to specify more than one value, e.g. category 1 or 2.
[](https://wger.readthedocs.io/en/latest/administration/gym.html "Gym administration") [Next ](https://wger.readthedocs.io/en/latest/api/routines.html "Using the routine API")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
