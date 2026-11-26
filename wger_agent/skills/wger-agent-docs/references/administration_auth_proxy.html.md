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
  * Authentication Proxy (SSO)
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/administration/auth_proxy.rst)


* * *
# Authentication Proxy (SSO)[](https://wger.readthedocs.io/en/latest/administration/auth_proxy.html#authentication-proxy-sso "Link to this heading")
This feature allows you to delegate user authentication to a trusted reverse proxy server (e.g., Nginx, Caddy, Apache, Traefik) or an external authentication provider (e.g., Authelia, Authentik, Keycloak, systems using LDAP, SAML, OAuth2) fronting the application.
When enabled, if the trusted proxy successfully authenticates a user and sets a specific HTTP header containing their username, wger will automatically log that user in. If the user doesn’t exist, it can optionally be created automatically.
Warning
Misconfiguration of this feature can lead to severe security vulnerabilities, potentially allowing attackers to impersonate any user!
The core risk is that an attacker could directly send the authentication header (e.g., `X-Remote-User: admin`) to the application, bypassing the proxy’s authentication, and gain access as that user. Because of this, your reverse proxy **must** be configured to overwrite the authentication header from any incoming request before it processes the request, e.g. pseudocode for Caddy:
```
your.wger.domain.com {
    # ... authentication configuration (e.g., forward_auth to Authelia/Authentik) ...
    # Assuming auth service sets Upstream-User header upon success

    reverse_proxy http://<wger_backend_ip>:<port> {

        # Remove header
        header_up header_up delete X-Remote-User

        # Set header based on auth service response
        header_up +X-Remote-User {http.reverse_proxy.upstream.header.Upstream-User}
    }
}

```

If you plan to use the mobile app, make sure to bypass the `api/*` subfolder from your proxy auth so that the app can access the api endpoint. In caddy, it might look something like this:
```
wger.example.com {
  import cert
  # allow api path to bypass auth (requires api key)
  handle /api/* {
    reverse_proxy wger_server:8000
  }
    # Enclosing in `route` forces execution order
    route {
        # Forward outpost path to actual outpost
        reverse_proxy /outpost.goauthentik.io/* authentik_server:9000
  ...
}

```

**Settings**

AUTH_PROXY_HEADER

(_required_) The name of the HTTP header that the reverse proxy sets with the authenticated user’s username. Usually `Remote-User`, but can be any name you choose. If set to an empty string (the default), the authentication proxy feature is disabled. Add the name according to the django logic when accessing headers: convert all characters to uppercase, replace any hyphens with underscores and add an `HTTP_` prefix to the name. So if the header is `Remote-User` set here `HTTP_X_REMOTE_USER`

AUTH_PROXY_TRUSTED_IPS

(_required_) A list of trusted IP addresses from which the application will accept authentication headers. Usually this will be the IP address of your reverse proxy. If the proxy is on the same host, include `127.0.0.1` and/or `::1`.

AUTH_PROXY_CREATE_UNKNOWN_USER

A boolean value that determines whether to automatically create a new user account if the authenticated user does not exist in the database. Default is false.

AUTH_PROXY_USER_EMAIL_HEADER

If set, the content of this header will be used as the email for newly created users (is ignored if `AUTH_PROXY_CREATE_UNKNOWN_USER` is not set). Same django name conventions as with `AUTH_PROXY_HEADER` apply.

AUTH_PROXY_USER_NAME_HEADER

If set, the content of this header will be used as the name for newly created users (is ignored if `AUTH_PROXY_CREATE_UNKNOWN_USER` is not set). Same django name conventions as with `AUTH_PROXY_HEADER` apply.
[](https://wger.readthedocs.io/en/latest/administration/settings.html "Settings") [Next ](https://wger.readthedocs.io/en/latest/administration/gym.html "Gym administration")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
