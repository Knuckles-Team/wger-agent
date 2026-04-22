[ wger project ](https://wger.readthedocs.io/en/latest/index.html)
latest  stable  2.4  2.0  1.9
Manual
  * [Using the routines](https://wger.readthedocs.io/en/latest/manual/routines.html)


Installation (prod)
  * [Docker compose](https://wger.readthedocs.io/en/latest/production/docker.html)
  * [Manual installation](https://wger.readthedocs.io/en/latest/production/installation.html)


Development
  * [Backend](https://wger.readthedocs.io/en/latest/development/backend.html)
  * [](https://wger.readthedocs.io/en/latest/development/frontend.html)
    * [Getting Started](https://wger.readthedocs.io/en/latest/development/frontend.html#getting-started)
    * [Release process](https://wger.readthedocs.io/en/latest/development/frontend.html#release-process)
    * [Rendering in django](https://wger.readthedocs.io/en/latest/development/frontend.html#rendering-in-django)
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
  * Frontend
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/development/frontend.rst)


* * *
# Frontend[](https://wger.readthedocs.io/en/latest/development/frontend.html#frontend "Link to this heading")
Note that “frontend” is not completely correct, more like “part of the frontend”. The application uses django to render the main page, react is only used for some parts of the application that need to be more interactive. These parts have their own repository which can be found at
<https://github.com/wger-project/react>
## Getting Started[](https://wger.readthedocs.io/en/latest/development/frontend.html#getting-started "Link to this heading")
Copy `.env.TEMPLATE` to `.env.development` and edit it to your needs.
You can obviously use your own instance, but feel free to use the test server (the db is reset every day):
  * URL: `https://wger-master.rge.uber.space`
  * username: `user`
  * password: `flutteruser`
  * API key: `31e2ea0322c07b9df583a9b6d1e794f7139e78d4`


Install node (>22) and run:
```
npm install

```

Then, in the project directory, you can run:
```
npm start

```

and open <http://localhost:3000> in the browser.
To run the tests:
```
npm run test

```

## Release process[](https://wger.readthedocs.io/en/latest/development/frontend.html#release-process "Link to this heading")
Update the version in `package.json` to use the current date:
```
NEW_VERSION=$(date +%Y-%m-%d)
npm version "${NEW_VERSION}" --no-git-tag-version

```

Publish the new version to npm by manually triggering the workflow `publish` in the github actions tab.
In the django server, update the version in `package.json` to the same version and run:
```
npm install

```

## Rendering in django[](https://wger.readthedocs.io/en/latest/development/frontend.html#rendering-in-django "Link to this heading")
We don’t render the whole page with react, just a part of it. We use `ReactView` in django to render an empty div with a known ID and then let react take over.
Take a look at `src/index.tsx` to see how we do this.
If you want to test the new version locally, you can use `npm link` which will create a symlink to the dev repository and allow you to instantly see the changes:
```
cd /path/to/react/repo
npm link
cd /path/to/wger/server
npm link @wger-project/react-components

```

Don’t forget to unlink everything once you’re done:
```
cd /path/to/wger/server
npm unlink @wger-project/react-components
cd /path/to/react/repo
npm unlink

```

[](https://wger.readthedocs.io/en/latest/development/backend.html "Backend") [Next ](https://wger.readthedocs.io/en/latest/development/mobile_app.html "Mobile App")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**Augment Code Review** Outperforms Cursor by 20% on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10130/019cbbb2-9e62-7721-9fcc-0146d8768cf1/)
