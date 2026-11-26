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
  * [](https://wger.readthedocs.io/en/latest/contributing.html)
    * [](https://wger.readthedocs.io/en/latest/contributing.html#code)
      * [Backend](https://wger.readthedocs.io/en/latest/development/backend.html)
      * [Frontend](https://wger.readthedocs.io/en/latest/development/frontend.html)
      * [Mobile App](https://wger.readthedocs.io/en/latest/development/mobile_app.html)
    * [Exercises](https://wger.readthedocs.io/en/latest/contributing.html#exercises)
    * [Translations](https://wger.readthedocs.io/en/latest/contributing.html#translations)
    * [Support the Project](https://wger.readthedocs.io/en/latest/contributing.html#support-the-project)
  * [Changelog](https://wger.readthedocs.io/en/latest/changelog.html)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * Contributing
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/contributing.rst)


* * *
# Contributing[](https://wger.readthedocs.io/en/latest/contributing.html#contributing "Link to this heading")
First off, thanks for taking the time to contribute! ❤️
Our goal is to build an awesome and flexible fitness and nutrition manager, along with a comprehensive list of exercises and ingredients, all released under a free license.
All types of contributions are encouraged. And if you like the project but just don’t have time to contribute, that’s fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
  * Talk about it on social media, at local meetups, or tell your friends/gym bros
  * Consider [supporting us with a donation](https://wger.readthedocs.io/en/latest/contributing.html#donation)
  * Star the project on GitHub


## Code[](https://wger.readthedocs.io/en/latest/contributing.html#code "Link to this heading")
Obviously, you can also contribute code. Before starting working on a new feature, please open an issue to discuss it with us. This is important to avoid duplicating work and to make sure that your contribution is in line with the project’s goals. A good starting point could be the roadmap for the next release:
> <https://github.com/orgs/wger-project/projects/5>
This application has three main repositories, each with its own purpose (and quirks) and its own section describing how to set up a development environment:
  * [Backend](https://wger.readthedocs.io/en/latest/development/backend.html)
  * [Frontend](https://wger.readthedocs.io/en/latest/development/frontend.html)
  * [Mobile App](https://wger.readthedocs.io/en/latest/development/mobile_app.html)


In any case you should have a basic grasp of git and GitHub, as well as how to create pull requests. If you are not familiar with these concepts, please consult one of the many online resources available, such as
  * <https://docs.github.com/en/pull-requests>
  * <https://docs.github.com/en/get-started/git-basics>


Make sure to always use a feature branch, even if the change is minor.
Once you have the code ready:
  * make sure to write good commit messages. A good commit message should explain what the change is about and why it was made.
  * make sure the tests are running (`python3 manage.py test` in the case of python). At the latest you will notice they are failing when you open the pull request, but it is better to check them before.
  * if you write new code, write new tests. These don’t need to test absolutely everything, but they should cover the most important parts of the code. If you are not sure what or how to test, just ask us.
  * make sure the code is formatted correctly (`ruff format && isort .` for python) and has a line length of 100 characters or less.
  * think about UI/UX. If you are adding a new feature, make sure it is easy to use and understand. Nobody here is a designer, but we try our best!
  * finally open a new PR. You can expect a response from a maintainer within a week, if you haven’t heard anything by then, ping the thread.
  * don’t mix different features in the same pull request. If you have multiple changes, just create a separate pull request for each one.


Also, these are mostly guidelines, not rules. As everywhere in life, use your best judgment, and feel free to propose changes to this document in a pull request.
Is this the first time you contribute to an open source project? No problem! Feel free to ping us if you need help setting everything up, it can be very overwhelming at first. We are happy to help you get started.
## Exercises[](https://wger.readthedocs.io/en/latest/contributing.html#exercises "Link to this heading")
You can contribute new exercises, images or videos, and edit or translate the existing ones. These contributions are just as important as code contributions, as they help improve the overall quality and usability of the application. Please use the search before to make sure your exercise doesn’t already exist.
Note that your account must be at least 3 weeks old and have a verified email.
## Translations[](https://wger.readthedocs.io/en/latest/contributing.html#translations "Link to this heading")
You can help translate the application online using Weblate and help make the application more accessible. To start just visit
> <https://hosted.weblate.org/engage/wger>
## Support the Project[](https://wger.readthedocs.io/en/latest/contributing.html#support-the-project "Link to this heading")
This project is free and open-source, but running it isn’t! Your support helps keep the server running, funds new development, and improves the overall experience for everyone. If you enjoy using this app, please consider making a small contribution. Every bit helps!
> <https://www.buymeacoffee.com/wger>
Thank you for supporting open-source fitness & nutrition tools! 🙌
[](https://wger.readthedocs.io/en/latest/api/routines.html "Using the routine API") [Next ](https://wger.readthedocs.io/en/latest/changelog.html "Changelog")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
