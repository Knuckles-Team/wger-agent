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
  * [](https://wger.readthedocs.io/en/latest/changelog.html)
    * [2.4](https://wger.readthedocs.io/en/latest/changelog.html#id1)
    * [](https://wger.readthedocs.io/en/latest/changelog.html#id2)
      * [🔧 Upgrade steps from 2.2](https://wger.readthedocs.io/en/latest/changelog.html#upgrade-steps-from-2-2)
      * [🚀 Features](https://wger.readthedocs.io/en/latest/changelog.html#features)
    * [](https://wger.readthedocs.io/en/latest/changelog.html#id3)
      * [🔧 Upgrade steps from 2.1](https://wger.readthedocs.io/en/latest/changelog.html#upgrade-steps-from-2-1)
      * [🚀 Features](https://wger.readthedocs.io/en/latest/changelog.html#id4)
      * [🧰 Maintenance](https://wger.readthedocs.io/en/latest/changelog.html#maintenance)
      * [🐛 Bug Fixes](https://wger.readthedocs.io/en/latest/changelog.html#bug-fixes)
    * [2.1](https://wger.readthedocs.io/en/latest/changelog.html#id49)
    * [2.0](https://wger.readthedocs.io/en/latest/changelog.html#id68)
    * [1.9](https://wger.readthedocs.io/en/latest/changelog.html#id111)
    * [1.8](https://wger.readthedocs.io/en/latest/changelog.html#id121)
    * [1.7](https://wger.readthedocs.io/en/latest/changelog.html#id160)
    * [1.6.1](https://wger.readthedocs.io/en/latest/changelog.html#id186)
    * [1.6](https://wger.readthedocs.io/en/latest/changelog.html#id187)
    * [1.5](https://wger.readthedocs.io/en/latest/changelog.html#id212)
    * [1.4](https://wger.readthedocs.io/en/latest/changelog.html#id231)
    * [1.3](https://wger.readthedocs.io/en/latest/changelog.html#id232)
    * [1.2](https://wger.readthedocs.io/en/latest/changelog.html#id233)
    * [1.1.1](https://wger.readthedocs.io/en/latest/changelog.html#id234)
    * [1.1](https://wger.readthedocs.io/en/latest/changelog.html#id235)
    * [1.0.3](https://wger.readthedocs.io/en/latest/changelog.html#id236)
    * [1.0.2](https://wger.readthedocs.io/en/latest/changelog.html#id237)
    * [1.0.1](https://wger.readthedocs.io/en/latest/changelog.html#id238)
    * [1.0](https://wger.readthedocs.io/en/latest/changelog.html#id239)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * Changelog
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/changelog.rst)


* * *
# Changelog[](https://wger.readthedocs.io/en/latest/changelog.html#changelog "Link to this heading")
## 2.4[](https://wger.readthedocs.io/en/latest/changelog.html#id1 "Link to this heading")
**2026-01-18**
See <https://github.com/wger-project/wger/releases/tag/2.4>
## 2.3[](https://wger.readthedocs.io/en/latest/changelog.html#id2 "Link to this heading")
**2025-04-05**
### 🔧 Upgrade steps from 2.2[](https://wger.readthedocs.io/en/latest/changelog.html#upgrade-steps-from-2-2 "Link to this heading")
  * Update python libraries `pip3 install -r requirements.txt`
  * Migrate database `python manage.py migrate`
  * Update CSS and JS libraries `yarn install`
  * Compile the CSS `yarn build:css:sass`
  * Update static files (only production): `python3 manage.py collectstatic`


### 🚀 Features[](https://wger.readthedocs.io/en/latest/changelog.html#features "Link to this heading")
  * Axes behind reverse proxy by [@bbkz](https://github.com/bbkz) in #1521
  * Fix wrong default setting in docker image by [@bbkz](https://github.com/bbkz) in #1531
  * Add sync method for ingredients by [@rolandgeider](https://github.com/rolandgeider) in #1546
  * Add progress bar to load-online-fixtures by [@ebwinters](https://github.com/ebwinters) in #1561
  * Move to pyproject.toml by [@rolandgeider](https://github.com/rolandgeider) in #1565
  * Add full text search by [@rolandgeider](https://github.com/rolandgeider) in #1594
  * put building/obtaining image instructions before trying to run it. by [@Dieterbe](https://github.com/Dieterbe) in #1655
  * add support for fiber goal by [@Dieterbe](https://github.com/Dieterbe) in #1664
  * Add myself to the Polish translators by [@Maniues](https://github.com/Maniues) in #1661
  * fix calendar accordion by [@bbkz](https://github.com/bbkz) in #1681
  * Refactor product/ingredient import by [@rolandgeider](https://github.com/rolandgeider) in #1666
  * Export prometheus metrics by [@rolandgeider](https://github.com/rolandgeider) in #1685
  * Fixed a typo by [@JLaField](https://github.com/JLaField) in #1695
  * Allow deactivating the language filter when searching for ingredients and exercises by [@rolandgeider](https://github.com/rolandgeider) in #1687
  * docker image: support loading exercise videos, fixtures, nutrition info by [@Dieterbe](https://github.com/Dieterbe) in #1746
  * Allow env specification of Redis connection SSL parameters by [@taylor-fuller](https://github.com/taylor-fuller) in #1751
  * Improve docker image by [@rolandgeider](https://github.com/rolandgeider) in #1786
  * give dummy meals names by [@Dieterbe](https://github.com/Dieterbe) in #1795
  * Update django.po by [@victorbmlabs](https://github.com/victorbmlabs) in #1798
  * Dynamically update WeightUnit from user preferences when creating workout by [@kmoy1](https://github.com/kmoy1) in #1807
  * Rework the calendar page by [@rolandgeider](https://github.com/rolandgeider) in #1824
  * make __main__ use pyinvoke `Program` as entrypoint by [@eyJhb](https://github.com/eyJhb) in #1833
  * Fix incorrectly placed <h1> tag and replace it with an <h4> tag for the “Members List” DataTable. by [@navyjosh](https://github.com/navyjosh) in #1843
  * Fix/registration by [@Maralai](https://github.com/Maralai) in #1855
  * fixes #1278 by [@blsouthcott](https://github.com/blsouthcott) in #1365
  * Add Management Command for Async Ingredient Synchronization by [@crypto-a](https://github.com/crypto-a) in #1876
  * Add language filter to sync-ingredients management command. by [@navyjosh](https://github.com/navyjosh) in #1875
  * Fixes for adding language filter to sync-ingredients management command. by [@scrapcode](https://github.com/scrapcode) in #1894
  * Clean apt temporary files in the base Docker image by [@PeterDaveHello](https://github.com/PeterDaveHello) in #1906
  * Flexible routines by [@rolandgeider](https://github.com/rolandgeider) in #1827


## 2.2[](https://wger.readthedocs.io/en/latest/changelog.html#id3 "Link to this heading")
**2023-11-06**
<https://github.com/wger-project/wger/releases/tag/2.2>
### 🔧 Upgrade steps from 2.1[](https://wger.readthedocs.io/en/latest/changelog.html#upgrade-steps-from-2-1 "Link to this heading")
  * Update python libraries `pip3 install -r requirements.txt`
  * Migrate database `python manage.py migrate`
  * Update CSS and JS libraries `yarn install`
  * Compile the CSS `yarn build:css:sass`
  * Update static files (only production): `python3 manage.py collectstatic`
  * Load new permissions `python3 manage.py loaddata groups.json categories.json`
  * Read the section on celery in this documentation on how to set it up. While at the moment this is not needed and only provides quality of life features, in the future this might change


### 🚀 Features[](https://wger.readthedocs.io/en/latest/changelog.html#id4 "Link to this heading")
  * Improvements to the nutritional plan handling. Users don’t have to setup a detailed plan with meals anymore, instead they can just log their meals [#817](https://github.com/wger-project/wger/issues/817)
  * Allow users to set goals for their nutritional plans. This basically works like the sum of the individual meals, but is simpler and easier to setup [#1003](https://github.com/wger-project/wger/issues/1003)
  * Implemented nutrition page with react
  * Added general measurements tracking to the web application [#875](https://github.com/wger-project/wger/issues/875)
  * Added JWT authentication to the REST API (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1047](https://github.com/wger-project/wger/issues/1047)
  * Added images to ingredients. This can now be shown in the nutritional plan, the autocompleter, etc. [#653](https://github.com/wger-project/wger/issues/653)
  * Add a celery queue for longer running or periodic tasks. At the moment this is only used to keep the exercises in sync and download the ingredient images, but other features are planned [#1174](https://github.com/wger-project/wger/issues/1174)
  * When scanning a product, fetch the data from the live OFF server if it is not found locally [#1012](https://github.com/wger-project/wger/issues/1012), [#1348](https://github.com/wger-project/wger/issues/1348)
  * Added brute protection against brute force login attacks (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1096](https://github.com/wger-project/wger/issues/1096)
  * Reworked the landing page (thanks [@12people](https://github.com/12people)!) [#1112](https://github.com/wger-project/wger/issues/1112)
  * Allow to set the minimum account age for users to contribute exercises (thanks [@mohammadrafigh](https://github.com/mohammadrafigh)!) [#1187](https://github.com/wger-project/wger/issues/1187)
  * Document the API with openAPI, redoc and all the goodies that come from it (better online docs, being able to generate clients, etc.) [#1127](https://github.com/wger-project/wger/issues/1127)
  * Allow searching exercises and ingredient in English in addition to the user’s currently selected language [#1238](https://github.com/wger-project/wger/issues/1238)
  * More flexible user (sub)locale switching. This specially affected English users that would be shown dates in US format [#1245](https://github.com/wger-project/wger/issues/1245)
  * Add a deletion log for exercises. This allows exercises to be marked as deleted by the system. Alternatively a replacement can be set so that when other instances sync the exercises logs and routines are correctly updated [#1237](https://github.com/wger-project/wger/issues/1237)
  * Show all the authors of an exercise and any of its child items (translations, images, videos, etc.) [#1137](https://github.com/wger-project/wger/issues/1137)
  * Allow users to give meals a description (thanks [@mohammadrafigh](https://github.com/mohammadrafigh)!) [#822](https://github.com/wger-project/wger/issues/822)
  * Added style field (Photo, 3D, etc.) to exercise image (thanks [@LucasSD](https://github.com/LucasSD)!) [#822](https://github.com/wger-project/wger/issues/822)
  * Added exercise edit history (thanks [@ImTheTom](https://github.com/ImTheTom)!) [#1082](https://github.com/wger-project/wger/issues/1082)
  * Added JWT authentication to rest API (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1134](https://github.com/wger-project/wger/issues/1134)
  * Add support for sub-locales in the application such as en-gb [#1275](https://github.com/wger-project/wger/issues/1275)
  * Moved some parts of routine management to react [#1328](https://github.com/wger-project/wger/issues/1328)


### 🧰 Maintenance[](https://wger.readthedocs.io/en/latest/changelog.html#maintenance "Link to this heading")
  * Improvements to the Open Food Facts product importer. The setup has been simplified with a docker compose, making the process much more streamlined. [#1505](https://github.com/wger-project/wger/issues/1505)
  * [#1137](https://github.com/wger-project/wger/issues/1137) (thanks [@AdamPetik](https://github.com/AdamPetik)!)
  * Show last modified datetime of exercises in the API [#1387](https://github.com/wger-project/wger/issues/1387)
  * Better handling of exercises without translations [#1319](https://github.com/wger-project/wger/issues/1319)
  * Split the dummy generator into individual files [#919](https://github.com/wger-project/wger/issues/919)
  * Update bootstrap to current version [#1109](https://github.com/wger-project/wger/issues/1109)
  * Update django to current version [#1110](https://github.com/wger-project/wger/issues/1110)
  * Bettler handling of exercises UUIDs (thanks [@Gr8ayu](https://github.com/Gr8ayu)) [#675](https://github.com/wger-project/wger/issues/675)
  * Add foreign key to meals on log (thanks [@Alig1493](https://github.com/Alig1493)) [#842](https://github.com/wger-project/wger/issues/842)
  * Make URL for media, static and login redirect configurable (thanks [@novalis111](https://github.com/novalis111)) [#1020](https://github.com/wger-project/wger/issues/1020)
  * Configure django axes (thanks [@RohanKaran](https://github.com/RohanKaran)) [#1143](https://github.com/wger-project/wger/issues/1143)
  * Add tzdate package to docker base image (thanks [@bbkz](https://github.com/bbkz)) [#1408](https://github.com/wger-project/wger/issues/1408)


### 🐛 Bug Fixes[](https://wger.readthedocs.io/en/latest/changelog.html#bug-fixes "Link to this heading")
  * Fix issue with django axes and mobile app [#1163](https://github.com/wger-project/wger/issues/1163)
  * Correctly format decimal places in numbers according to the user’s locale [#1402](https://github.com/wger-project/wger/issues/1402)
  * Fix issue when a user tried to register with an existing email via the app (thanks [@JayanthBontha](https://github.com/JayanthBontha)!) [#1459](https://github.com/wger-project/wger/issues/1459)
  * Fix bug in the demo entries generator (thanks [@JayanthBontha](https://github.com/JayanthBontha)!) [#1278](https://github.com/wger-project/wger/issues/1278)
  * Fix issue with password reset links and expired tokens (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1154](https://github.com/wger-project/wger/issues/1154)
  * Fix issue with password reset links and expired tokens (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1287](https://github.com/wger-project/wger/issues/1287)
  * Fix issue that prevented users from resetting their password (thanks [@RohanKaran](https://github.com/RohanKaran)!) [#1154](https://github.com/wger-project/wger/issues/1154)
  * Fix import error (thanks [@sophiamartelli](https://github.com/sophiamartelli)!) [#986](https://github.com/wger-project/wger/issues/986)
  * Use either TLS or SSL for emails (thanks [@bbkz](https://github.com/bbkz)!) [#1514](https://github.com/wger-project/wger/issues/1514)
  * Fix bug in the link used in the password reset link [#1320](https://github.com/wger-project/wger/issues/1320)
  * Fix bug in the weight log chart [#1308](https://github.com/wger-project/wger/issues/1308)


## 2.1[](https://wger.readthedocs.io/en/latest/changelog.html#id49 "Link to this heading")
**2022-10-11**
Upgrade steps from 2.0:
  * Install ffmpeg if you want to upload videos (consult documentation).
  * Update python libraries `pip3 install -r requirements.txt`
  * To sync the new exercises:
    * Run migrations `python3 manage.py migrate`
    * delete all exercises not in use `python manage.py delete-unused-exercises` (this will delete all exercises that are currently in the database but are not part of any workout, log, etc. You will be prompted before the script does anything)
    * get the new exercises `python manage.py sync-exercises` (Also note that if you don’t perform these steps and directly run a regular sync the worst that can happen is that you might have some duplicate exercises in your installation)
    * get the new images `python manage.py download-exercise-images`
    * get the new videos `python manage.py download-exercise-videos` (please note that this needs more space)
  * Update CSS and JS libraries `yarn install`
  * Compile the CSS `yarn build:css:sass`
  * Update static files (only production): `python3 manage.py collectstatic`
  * Load new permissions `python3 manage.py loaddata groups.json categories.json`


🚀 Features:
  * The exercise database has undergone a huge cleanup, combining duplicates and translations, deleting stubs, etc. Refreshed the UI for the exercise overview, detail view and contribution page. It is now easier (or at all possible) to submit, correct and translate the exercises. [#1120](https://github.com/wger-project/wger/pull/1120)
  * New gallery where users can upload pictures to track their progress [#572](https://github.com/wger-project/wger/issues/572)
  * Exercises can now have videos. Also many thanks to Goulart for providing 150 videos [#970](https://github.com/wger-project/wger/issues/970) and releasing them under the CC-BY-SA license.
  * Add templates / centrally managed workouts (thanks [@qwert45hi](https://github.com/qwert45hi)) [#639](https://github.com/wger-project/wger/issues/639)
  * Add comment filed to set for user notes [#702](https://github.com/wger-project/wger/issues/702)
  * Custom measurements such as biceps size or body fat [#133](https://github.com/wger-project/wger/issues/133)
  * Add picture type to exercise images (thanks [@LucasSD](https://github.com/LucasSD)) [#589](https://github.com/wger-project/wger/issues/589)
  * Add optional relation from nutritional diary to meal (thanks [@Alig1493](https://github.com/Alig1493)) [#819](https://github.com/wger-project/wger/issues/819)
  * Muscles now have a “common” name, besides their names in Latin (thanks [@ImTheTom](https://github.com/ImTheTom)) [#1041](https://github.com/wger-project/wger/pull/1041)
  * Allow to add nutritional plan diary entries for other dates (thanks [@ImTheTom](https://github.com/ImTheTom)) [#520](https://github.com/wger-project/wger/issues/520)


🐛 Bug Fixes:
  * Adding a new workout day no longer needs to be saved twice (thanks [@ImTheTom](https://github.com/ImTheTom)) [#974](https://github.com/wger-project/wger/issues/974)


🧰 Maintenance:
  * Exercise API response is now cached (thanks [@ImTheTom](https://github.com/ImTheTom)) [#1033](https://github.com/wger-project/wger/issues/1033)
  * Changes to the REST API:
    * /exercisebaseinfo/ - New endpoint to get exercise information grouped by the base exercise
    * /language/ - Also expose the language ID
    * /exerciseimage/ - `exercise` was renamed to `exercise_base` (was pointing there anyway) - New field `style`
    * /workout/ - `comment` was renamed to name - field `description` was added, for longer descriptions
    * /set/ - field `comment` added, for user notes
    * /nutritiondiary/ - field `meal` added, optional reference to meal
    * /min-app-version/ - New endpoint indicating minimum required version for flutter app
  * [#666](https://github.com/wger-project/wger/issues/666), [#667](https://github.com/wger-project/wger/issues/667), [#656](https://github.com/wger-project/wger/issues/656) (thanks [@jackmulligan-ire](https://github.com/jackmulligan-ire)), [#716](https://github.com/wger-project/wger/issues/716)


## 2.0[](https://wger.readthedocs.io/en/latest/changelog.html#id68 "Link to this heading")
**2021-05-01**
Upgrade steps from 1.9:
  * Update python libraries `pip3 install -r requirements.txt`
  * Install `yarn` and `sass` (e.g. `sudo npm install -g yarn sass`)
  * Update CSS and JS libraries `yarn install`
  * Compile the CSS `yarn build:css:sass`
  * Run migrations `python3 manage.py migrate`
  * Update data `python3 manage.py loaddata licenses.json languages.json language_config.json`
  * Load new ingredients (note that this will overwrite any ingredients that you might have added) `wger load-online-fixtures`
  * Update static files (only production): `python3 manage.py collectstatic`
  * Subcommands for `wger` now use dashes in their names (i.e. create-settings instead of create_settings)


🚀 Features:
  * Add nutrition diary to log the daily calories actually taken [#284](https://github.com/wger-project/wger/issues/284), [#501](https://github.com/wger-project/wger/issues/501) and [#506](https://github.com/wger-project/wger/issues/506) (thanks [@WalkingPizza](https://github.com/WalkingPizza) and [@oconnelc](https://github.com/oconnelc))
  * Support for reps-in-reserve (RiR) in workout plans and logs [#479](https://github.com/wger-project/wger/issues/479) (thanks [@SkyNetIndustry](https://github.com/SkyNetIndustry))
  * Improved user experience, on desktop and mobile [#337](https://github.com/wger-project/wger/issues/337)
  * Around 70000 new ingredients with Open Food Facts import with more to come [#422](https://github.com/wger-project/wger/issues/422) (thanks [@harlenesamra](https://github.com/harlenesamra), [@nikithamurikinati](https://github.com/nikithamurikinati) and [@jcho1](https://github.com/jcho1))
  * Group common exercise information such as muscles, etc. for more easy translations, data management, etc. [#448](https://github.com/wger-project/wger/issues/448) (thanks [@nikithamurikinati](https://github.com/nikithamurikinati), [@harlenesamra](https://github.com/harlenesamra), [@jcho17](https://github.com/jcho17), [@vaheeshta](https://github.com/vaheeshta) and [@jeevikaghosh](https://github.com/jeevikaghosh))
  * Group similar exercises such as wide grip, reverse, etc. [#555](https://github.com/wger-project/wger/issues/555) (thanks [@ryowright](https://github.com/ryowright))
  * Improved info endpoints for exercises and ingredients, this saves additional API calls [#411](https://github.com/wger-project/wger/issues/411)
  * Show BMI on weight graph [#462](https://github.com/wger-project/wger/issues/462) (thanks [@Svn-Sp](https://github.com/Svn-Sp))
  * Allow user to edit and delete body weight entries [#478](https://github.com/wger-project/wger/issues/478) (thanks [@beingbiplov](https://github.com/beingbiplov))
  * Show kJoules as well as kcal in nutritional plan [#568](https://github.com/wger-project/wger/issues/568) (thanks [@nopinter](https://github.com/nopinter) and [@derekli17](https://github.com/derekli17))
  * Check name similarity when adding exercises to avoid duplicates [#551](https://github.com/wger-project/wger/issues/551) (thanks [@lydiaxing](https://github.com/lydiaxing), [@eq8913](https://github.com/eq8913), [@Hita-K](https://github.com/Hita-K))
  * Return the muscle background images in the REST API [#547](https://github.com/wger-project/wger/issues/547) (thanks [@gengkev](https://github.com/gengkev))


🐛 Bug Fixes:
  * [#368](https://github.com/wger-project/wger/issues/368), [#379](https://github.com/wger-project/wger/issues/379), [#426](https://github.com/wger-project/wger/issues/426) (thanks [@austin-leung](https://github.com/austin-leung)), [#499](https://github.com/wger-project/wger/issues/499), [#505](https://github.com/wger-project/wger/issues/505), [#504](https://github.com/wger-project/wger/issues/504), [#511](https://github.com/wger-project/wger/issues/511), [#516](https://github.com/wger-project/wger/issues/516), [#522](https://github.com/wger-project/wger/issues/522), [#554](https://github.com/wger-project/wger/issues/554) and [#560](https://github.com/wger-project/wger/issues/560) (thanks [@sandilsranasinghe](https://github.com/sandilsranasinghe)), [#564](https://github.com/wger-project/wger/issues/564), [#565](https://github.com/wger-project/wger/issues/565), [#615](https://github.com/wger-project/wger/issues/615), [#560](https://github.com/wger-project/wger/issues/560) (thanks [@bradsk88](https://github.com/bradsk88)), [#617](https://github.com/wger-project/wger/issues/617) (thanks [@Sidrah-Madiha](https://github.com/Sidrah-Madiha)), [#636](https://github.com/wger-project/wger/issues/636), [#640](https://github.com/wger-project/wger/issues/640), [#642](https://github.com/wger-project/wger/issues/642), [#648](https://github.com/wger-project/wger/issues/648), [#650](https://github.com/wger-project/wger/issues/650)


🧰 Maintenance:
  * Moved translations to weblate [#266](https://github.com/wger-project/wger/issues/266)
  * Improved docker and docker-compose images [#340](https://github.com/wger-project/wger/issues/340)
  * Updated many libraries to the last version (bootstrap, font awesome, etc.)
  * Use yarn to download CSS/JS libraries
  * Improvements to documentation (e.g. [#494](https://github.com/wger-project/wger/issues/494))
  * Improved cache handling [#246](https://github.com/wger-project/wger/issues/246) (thanks [@louiCoder](https://github.com/louiCoder))
  * Others: [#450](https://github.com/wger-project/wger/issues/450) (thanks [@Rkamath2](https://github.com/Rkamath2)), [#631](https://github.com/wger-project/wger/issues/631) (thanks [@harlenesamra](https://github.com/harlenesamra)), [#664](https://github.com/wger-project/wger/issues/664) (thanks [@calvinrw](https://github.com/calvinrw)),


## 1.9[](https://wger.readthedocs.io/en/latest/changelog.html#id111 "Link to this heading")
**2020-06-29**
Upgrade steps from 1.8:
  * Django update to 3.x: `pip install -r requirements.txt`
  * Database upgrade: `python manage.py migrate`
  * Update static files (only production): `python manage.py collectstatic`


New features:
  * Allow users to enter their birthdate instead of just the age (thanks [@dtopal](https://github.com/dtopal)) [#332](https://github.com/wger-project/wger/issues/332)
  * Work to ensure that mobile templates are used when appropriate
  * Added optional S3 static asset hosting.
  * Drop Python 2 support.
  * Replaced django-mobile with django-user_agent (and some custom code) This isn’t as slick as django-mobile was, but it unblocks possible Django 2.x support.
  * Update many dependencies to current versions.


Improvements:
  * Improve the look of weight graph (thanks [@alokhan](https://github.com/alokhan)) [#381](https://github.com/wger-project/wger/issues/381)
  * Added password validation rules for more security
  * Exercise image downloader checks only accepted exercises (thanks [@gmmoraes](https://github.com/gmmoraes)) [#363](https://github.com/wger-project/wger/issues/363)
  * Use a native data type for the exercises’ UUID (thanks [@gmmoraes](https://github.com/gmmoraes)) [#364](https://github.com/wger-project/wger/issues/364)
  * Increase speed of testsuite by performing the tests in parallel (thanks [@Mbarak-Mbigo](https://github.com/Mbarak-Mbigo)) [wger_vulcan/#6](https://github.com/andela/wger_vulcan/pull/6)
  * Update screen when adding an exercise to the workout while using set slider (thanks [@gmmoraes](https://github.com/gmmoraes)) [#374](https://github.com/wger-project/wger/issues/374)
  * Work to slim docker image * Download images at startup - If DOWNLOAD_IMGS environmental variable is set to TRUE * Uninstall dev packages
  * Update Ubuntu version used in docker container.
  * Fixed a handful of hard coded static path references to use static taglib
  * Updated tinymce theme for v5.


Other improvements and bugfixes: [#336](https://github.com/wger-project/wger/issues/336), [#359](https://github.com/wger-project/wger/issues/359),`#386`_, [#443](https://github.com/wger-project/wger/issues/443)
## 1.8[](https://wger.readthedocs.io/en/latest/changelog.html#id121 "Link to this heading")
**2017-04-05**
Warning
There have been some changes to the installation procedure. Calling ‘invoke’ on its own has been deprecated, you should use the ‘wger’ command (which accepts the same options). Also, some of these commands have been renamed:
  * `start_wger` to `wger`
  * `bootstrap_wger` to `bootstrap`


Upgrade steps from 1.7:
  * Django update to 1.9: `pip install -r requirements.txt`
  * Database upgrade: `python manage.py migrate`
  * Reset cache: `python manage.py clear-cache --clear-all`
  * Due to changes in the JS package management, you have to delete wger/core/static/bower_components and do a `python manage.py bower install`
  * Update static files (only production): `python manage.py collectstatic`
  * Load new the languages fixtures as well as their configuration `python manage.py loaddata languages` and `python manage.py loaddata language_config`
  * New config option in settings.py: `WGER_SETTINGS['TWITTER']`. Set this if your instance has its own twitter account.


New languages:
  * Norwegian (many thanks to Kjetil Elde [@w00p](https://github.com/w00p) [#304](https://github.com/wger-project/wger/issues/304))
  * French (many thanks to all translators)


New features:
  * Big ingredient list in Dutch, many thanks to alphafitness.club!
  * Add repetition (minutes, kilometer, etc.) and weight options (kg, lb, plates, until failure) to sets [#216](https://github.com/wger-project/wger/issues/216) and [#217](https://github.com/wger-project/wger/issues/217)
  * Allow administrators to deactivate the guest user account [#330](https://github.com/wger-project/wger/issues/330)
  * Add option to show the gym name in the header instead of the application name, part of [#214](https://github.com/wger-project/wger/issues/214)
  * Exercise names are now capitalized, making them more consistent [#232](https://github.com/wger-project/wger/issues/232)
  * Much improved landing page (thanks [@DeveloperMal](https://github.com/DeveloperMal)) [#307](https://github.com/wger-project/wger/issues/307)
  * Add extended PDF options to schedules as well (thanks [@alelevinas](https://github.com/alelevinas) ) [#272](https://github.com/wger-project/wger/issues/272)
  * Show trained secondary muscles in workout view (thanks [@alokhan](https://github.com/alokhan) ) [#282](https://github.com/wger-project/wger/issues/282)
  * Use the metricsgraphics library to more easily draw charts [#188](https://github.com/wger-project/wger/issues/188)
  * Removed persona (browserID) as a login option, the service is being discontinued [#331](https://github.com/wger-project/wger/issues/331)


Improvements:
  * Check and enforce style guide for JS files [#317](https://github.com/wger-project/wger/issues/317) ([@petervanderdoes](https://github.com/petervanderdoes))
  * BMI calculator now works with pounds as well (thanks [@petervanderdoes](https://github.com/petervanderdoes)) [#318](https://github.com/wger-project/wger/issues/318)
  * Give feedback when autocompleter didn’t find any results [#293](https://github.com/wger-project/wger/issues/293)
  * Make exercise names links to their detail page in training log pages [#350](https://github.com/wger-project/wger/issues/350)
  * Better GUI consistency in modal dialogs (thanks [@jstoebel](https://github.com/jstoebel) ) [#274](https://github.com/wger-project/wger/issues/274)
  * Cache is cleared when editing muscles (thanks [@RyanSept](https://github.com/RyanSept) [@pythonGeek](https://github.com/pythonGeek) ) [#260](https://github.com/wger-project/wger/issues/260)
  * Fields in workout log form are no longer required, making it possible to only log weight for certain exercises [#334](https://github.com/wger-project/wger/issues/334)
  * New, more verbose, API endpoint for exercises, (thanks [@andela-bmwenda](https://github.com/andela-bmwenda))
  * The dashboard page was improved and made more user friendly [#201](https://github.com/wger-project/wger/issues/201) (partly)
  * Replace jquery UI’s autocompleter and sortable this reduces the size of JS and CSS [#78](https://github.com/wger-project/wger/issues/78) and [#79](https://github.com/wger-project/wger/issues/79)
  * Update to D3js v4 [#314](https://github.com/wger-project/wger/issues/314), [#302](https://github.com/wger-project/wger/issues/302)
  * Remove hard-coded CC licence from documentation and website [#247](https://github.com/wger-project/wger/issues/247)


Other improvements and bugfixes: [#25](https://github.com/wger-project/wger/issues/25), [#243](https://github.com/wger-project/wger/issues/243), [#279](https://github.com/wger-project/wger/issues/279), [#275](https://github.com/wger-project/wger/issues/275), [#270](https://github.com/wger-project/wger/issues/270), [#258](https://github.com/wger-project/wger/issues/258), [#257](https://github.com/wger-project/wger/issues/257), [#263](https://github.com/wger-project/wger/issues/263), [#269](https://github.com/wger-project/wger/issues/269), [#296](https://github.com/wger-project/wger/issues/296), [#297](https://github.com/wger-project/wger/issues/297), [#303](https://github.com/wger-project/wger/issues/303), [#311](https://github.com/wger-project/wger/issues/311), [#312](https://github.com/wger-project/wger/issues/312), [#313](https://github.com/wger-project/wger/issues/313), [#322](https://github.com/wger-project/wger/issues/322), [#324](https://github.com/wger-project/wger/issues/324), [#325](https://github.com/wger-project/wger/issues/325)
## 1.7[](https://wger.readthedocs.io/en/latest/changelog.html#id160 "Link to this heading")
**2016-02-28**
New translations:
  * Czech (many thanks to Tomáš Z.!)
  * Swedish (many thanks to ywecur!)


New features:
  * Workout PDF can now print the exercises’ images and comments [#261](https://github.com/wger-project/wger/issues/261)
  * Allow login with username or email (thanks [@warchildmd](https://github.com/warchildmd)) #164`_
  * Correctly use user weight when calculating nutritional plans’ calories (thanks [@r-hughes](https://github.com/r-hughes)) [#210](https://github.com/wger-project/wger/issues/210)
  * Fix problem with datepicker [#192](https://github.com/wger-project/wger/issues/192)
  * Order of exercises in supersets is not reverted anymore [#229](https://github.com/wger-project/wger/issues/229)
  * Improvements to the gym management:
    * Allow to add contracts to members
    * Visual consistency for lists and actions
    * Vastly reduce the number of database queries in gym member list [#144](https://github.com/wger-project/wger/issues/144)
    * Global list of users for installation [#212](https://github.com/wger-project/wger/issues/212)
    * Allow administrators to restrict user registration [#220](https://github.com/wger-project/wger/issues/220)
    * Refactored and improved code, among others [#208](https://github.com/wger-project/wger/issues/208)
    * Allow gym managers to reset a member’s password [#186](https://github.com/wger-project/wger/issues/186)
  * Better rendering of some form elements [#244](https://github.com/wger-project/wger/issues/244)
  * Improved GUI consistency [#149](https://github.com/wger-project/wger/issues/149)
  * Docker images for easier installation [#181](https://github.com/wger-project/wger/issues/181)
  * Use hostname for submitted exercises (thanks [@jamessimas](https://github.com/jamessimas)) [#159](https://github.com/wger-project/wger/issues/159)
  * Download js libraries with bowerjs (thanks [@tranbenny](https://github.com/tranbenny)) [#126](https://github.com/wger-project/wger/issues/126)
  * Improved and more flexible management commands [#184](https://github.com/wger-project/wger/issues/184)
  * Fixed error when importing weight entries from CSV (thanks [@r-hughes](https://github.com/r-hughes)) [#204](https://github.com/wger-project/wger/issues/204)
  * Fixed problems when building and installing the application on Windows (thanks [@romansp](https://github.com/romansp)) [#197](https://github.com/wger-project/wger/issues/197)
  * Fixed potential Denial Of Service attack (thanks [@r-hughes](https://github.com/r-hughes)) [#238](https://github.com/wger-project/wger/issues/238)
  * Dummy data generator can not create nutrition plans (thanks [@cthare](https://github.com/cthare)) [#241](https://github.com/wger-project/wger/issues/241)


Other improvements and bugfixes: [#279](https://github.com/wger-project/wger/issues/279), [#275](https://github.com/wger-project/wger/issues/275), [#270](https://github.com/wger-project/wger/issues/270), [#258](https://github.com/wger-project/wger/issues/258), [#257](https://github.com/wger-project/wger/issues/257)
## 1.6.1[](https://wger.readthedocs.io/en/latest/changelog.html#id186 "Link to this heading")
**2015-07-25**
Bugfix release
## 1.6[](https://wger.readthedocs.io/en/latest/changelog.html#id187 "Link to this heading")
**2015-07-25**
New translations:
  * Greek (many thanks to Mark Nicolaou!)


New features:
  * Save planned weight along with the repetitions [#119](https://github.com/wger-project/wger/issues/119)
  * Improvements to the workout calendar [#98](https://github.com/wger-project/wger/issues/98)
  * Allow external access to workouts and other pages to allow for sharing [#102](https://github.com/wger-project/wger/issues/102), [#124](https://github.com/wger-project/wger/issues/124)
  * Email reminder to regularly enter (body) weight entries [#115](https://github.com/wger-project/wger/issues/115)
  * Allow users to submit corrections to exercises
  * Add day detail view in workout calendar [#103](https://github.com/wger-project/wger/issues/103)
  * Fix bug where the exercises added to a superset did not remain sorted [#89](https://github.com/wger-project/wger/issues/89)
  * Reduce the size of generated HTML code [#125](https://github.com/wger-project/wger/issues/125)
  * Allow users to copy shared workouts from others [#127](https://github.com/wger-project/wger/issues/127)
  * Added breadbrumbs, to make navigation easier [#101](https://github.com/wger-project/wger/issues/101)
  * Add option to delete workout sessions and their logs [#156](https://github.com/wger-project/wger/issues/156)
  * Improve installation, development and maintenance documentation [#114](https://github.com/wger-project/wger/issues/114)


Other improvements and bugfixes: [#99](https://github.com/wger-project/wger/issues/99), [#100](https://github.com/wger-project/wger/issues/100), [#106](https://github.com/wger-project/wger/issues/106), [#108](https://github.com/wger-project/wger/issues/108), [#110](https://github.com/wger-project/wger/issues/110), [#117](https://github.com/wger-project/wger/issues/117), [#118](https://github.com/wger-project/wger/issues/118), [#128](https://github.com/wger-project/wger/issues/128), [#131](https://github.com/wger-project/wger/issues/131), [#135](https://github.com/wger-project/wger/issues/135), [#145](https://github.com/wger-project/wger/issues/145), [#155](https://github.com/wger-project/wger/issues/155)
## 1.5[](https://wger.readthedocs.io/en/latest/changelog.html#id212 "Link to this heading")
**2014-12-16**
New Translations:
  * Dutch (many thanks to David Machiels!)
  * Portuguese (many thanks to Jefferson Campos!) [#97](https://github.com/wger-project/wger/issues/97)


New features:
  * Add support for gym management [#85](https://github.com/wger-project/wger/issues/85)
    * Gym managers can create and manage gyms
    * Trainers can see the gym’s users and their routines
  * Reduce the amount of CSS and JS libraries by using bootstrap as much as possible [#73](https://github.com/wger-project/wger/issues/73)
  * Improvements to the REST API [#75](https://github.com/wger-project/wger/issues/75)
    * Add read-write access
    * Add live browsing of the API with django rest framework
    * Improve documentation
    * /api/v1 is marked deprecated
  * Show exercise pictures in workout as well
  * Detailed view of exercises and workouts in schedule [#86](https://github.com/wger-project/wger/issues/86)
  * Support for both metric (kg) and imperial (lb) weight units [#105](https://github.com/wger-project/wger/issues/105)
  * Allow the user to delete his account and data [#84](https://github.com/wger-project/wger/issues/84)
  * Add contact field to feedback form
  * Cleanup translation strings [#94](https://github.com/wger-project/wger/issues/94)
  * Python 3 compatibility! [#68](https://github.com/wger-project/wger/issues/68)


Other improvements and bugfixes: [#51](https://github.com/wger-project/wger/issues/51), [#76](https://github.com/wger-project/wger/issues/76), [#80](https://github.com/wger-project/wger/issues/80), [#81](https://github.com/wger-project/wger/issues/81), [#82](https://github.com/wger-project/wger/issues/82), [#91](https://github.com/wger-project/wger/issues/91), [#92](https://github.com/wger-project/wger/issues/92), [#95](https://github.com/wger-project/wger/issues/95), [#96](https://github.com/wger-project/wger/issues/96)
## 1.4[](https://wger.readthedocs.io/en/latest/changelog.html#id231 "Link to this heading")
**2014-03-08**
New features and bugfixes:
>   * Calendar view to more easily check workout logs
>   * Add “gym mode” with timer to log the workout while at the gym
>   * Add automatic email reminders for new workouts
>   * New iCal export to add workouts and schedules e.g. to google calendar
>   * New exercise overview, grouped by equipment
>   * Add possibility to write comments and rate the workout
>   * Simplify form for new exercises
>   * Alternative PDF export of workout without table for entering logs
>   * Unified way of specifying license of submitted content (exercises, etc.)
>

## 1.3[](https://wger.readthedocs.io/en/latest/changelog.html#id232 "Link to this heading")
**2013-11-27**
New translations:
>   * Bulgarian (many thanks to Lyuboslav Petrov!)
>   * Russian (many thanks to Inna!)
>   * Spanish
>

New features and bugfixes:
>   * Mobile version of website
>   * Add images to the exercises
>   * Exercises now can list needed equipment (barbell, etc.)
>   * BMI calculator
>   * Daily calories calculator
>   * New management utility for languages
>   * Improved performance
>   * RESTful API
>

## 1.2[](https://wger.readthedocs.io/en/latest/changelog.html#id233 "Link to this heading")
**2013-05-19**
New features and bugfixes:
>   * Added scheduling option for workouts.
>   * Open all parts of website to all users, this is done by a custom middleware
>   * Regular users can submit exercises and ingredients to be included in the general list
>   * Add more ‘human’ units to ingredients like ‘1 cup’ or ‘1 slice’
>   * Add nutritional values calculator on the ingredient detail page
>   * Several bugfixes
>   * Usability improvements
>

## 1.1.1[](https://wger.readthedocs.io/en/latest/changelog.html#id234 "Link to this heading")
**2013-03-06**
New features and bugfixes:
>   * Pin version of app django_browserid due to API changes in 0.8
>   * Fix issue with tabs on exercise overview due to API changes in JQuery
>

## 1.1[](https://wger.readthedocs.io/en/latest/changelog.html#id235 "Link to this heading")
**2013-02-23**
New features and bugfixes:
>   * Better navigation bar
>   * Added descriptions for the exercises (German)
>   * New workout logbook, to keep track of your improvements
>   * Import your weight logs from a spreadsheet (CSV-Import)
>   * Better filtering for weight chart
>   * Muscle overview with corresponding exercises
>   * Add guest accounts by generating a temporary user
>   * Description pages about the software
>   * Easier installation process
>

## 1.0.3[](https://wger.readthedocs.io/en/latest/changelog.html#id236 "Link to this heading")
**2012-11-19**
New features and bugfixes:
>   * Add option to copy (duplicate) workouts and nutritional plans
>   * Login without an account with Mozilla’s Persona (BrowserID)
>   * Better AJAX handling of the modal dialogs, fewer page reloads and redirects
>   * Expand the list of ingredients in German
>   * Add pagination to the ingredient list
>   * Improvements to user page:
>     * Add a “reset password” link to the login page
>     * Email is now user-editable
>   * More natural lines in weight chart with cubic interpolation
>

## 1.0.2[](https://wger.readthedocs.io/en/latest/changelog.html#id237 "Link to this heading")
**2012-11-02**
Bugfix release
## 1.0.1[](https://wger.readthedocs.io/en/latest/changelog.html#id238 "Link to this heading")
**2012-11-02**
New features and bugfixes:
>   * Fix issue with password change
>   * Small improvements to UI
>   * Categories editable/deletable from the exercise overview page
>   * Exercise AJAX search groups by category
>   * More tests!
>   * Use generic views for editing, creating and deleting objects
>

## 1.0[](https://wger.readthedocs.io/en/latest/changelog.html#id239 "Link to this heading")
**2012-10-16**
Initial release.
New features and bugfixes:
>   * Workout manager
>   * PDF output for logging progress
>   * Initial data with the most popular exercises
>   * Simple weight chart
>   * Nutrition plan manager
>   * Simple PDF output
>   * Initial data with nutritional values from the USDA
>

[](https://wger.readthedocs.io/en/latest/contributing.html "Contributing")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
