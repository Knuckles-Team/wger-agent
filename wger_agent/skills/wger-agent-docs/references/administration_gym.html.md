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
  * [](https://wger.readthedocs.io/en/latest/administration/gym.html)
    * [Member Management](https://wger.readthedocs.io/en/latest/administration/gym.html#member-management)
    * [Contracts](https://wger.readthedocs.io/en/latest/administration/gym.html#contracts)
    * [E-Mails](https://wger.readthedocs.io/en/latest/administration/gym.html#e-mails)
    * [](https://wger.readthedocs.io/en/latest/administration/gym.html#configuration)
      * [Inactive members](https://wger.readthedocs.io/en/latest/administration/gym.html#inactive-members)
      * [Gym name in the header](https://wger.readthedocs.io/en/latest/administration/gym.html#gym-name-in-the-header)


API
  * [Using the API](https://wger.readthedocs.io/en/latest/api/api.html)
  * [Using the routine API](https://wger.readthedocs.io/en/latest/api/routines.html)


All the rest
  * [Contributing](https://wger.readthedocs.io/en/latest/contributing.html)
  * [Changelog](https://wger.readthedocs.io/en/latest/changelog.html)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * Gym administration
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/administration/gym.rst)


* * *
# Gym administration[](https://wger.readthedocs.io/en/latest/administration/gym.html#gym-administration "Link to this heading")
wger provides support for managing both gyms and members. For example, trainers/coaches can follow their students progress, and gym managers are able to keep track of their members contracts.
If the installation is being used for a single gym, you can set the default gym in the global configuration options in the gym list. This will update all existing users as well as newly registered ones so they belong to that gym.
There are 3 groups used for the different administrative roles:
  * **General Manager:** Can manage (add, edit, delete) the different gyms for the installation as well as add gym managers, trainers, and members but is not allowed to see the members’ workout data.
  * **Gym Manager:** Can manage the users for a single gym (editing, deactivating, and adding contracts, etc.).
  * **Trainer:** Can manage the workouts and other data for the members of a single gym.


These roles are not mutually exclusive, if your workflow demands it, you can combine all three roles into one account.
Except for general managers, administrative users belong to a single gym (the one they were created in) and can access only those members. This setting cannot be changed later. The user’s gym appears in the top-right menu.
## Member Management[](https://wger.readthedocs.io/en/latest/administration/gym.html#member-management "Link to this heading")
To add members to a gym:
  1. Click the `Add Member` button at the top of the member overview.
  2. Fill in the form to generate a password for the user.
  3. Save this password and give it to the user and it cannot be retrieved later.


> OR
  1. Click the `Add Member` button at the top of the member overview.
  2. Instruct new members to use the reset password links when logging in for the first time.


To export all gym members:
  1. Navigate to the `Actions` button on the gym detail page.
  2. Here, you are provided with a CSV file that can be imported into a spreadsheet program for further processing.


Trainers can click on a user and access an overview of the user’s workouts, body weights, nutrition plans, etc. When clicking on the “log in as this user”, the trainer can assume the identity of the user to create new workouts for example. Additionally, Trainers can add notes and upload documents related to individual members. A note is a free text, while a document can be any file. This information can be used to save information on specific injuries or other important notes related to the member. Note that these entries are not accessible by the members themselves, but only by the trainers.
Individual members can be deactivated by clicking on the “actions” button on the top of the member’s detail table. Deactivated users can’t log in, but are not deleted from the system and can be reactivated at any time in the future. If you wish to completely delete a user from the system, use the “delete” option but keep in mind that this action cannot be undone.
## Contracts[](https://wger.readthedocs.io/en/latest/administration/gym.html#contracts "Link to this heading")
It is also possible to manage the members’ contracts with the application. A contract is composed of a base form and optional _type_ and _options_. The type is a single attribute, such as “Student contract” or “Special offer 2016”. The options are basically the same but more than one can be selected at once and can be used for items that can e.g. be booked in addition to the default contract such as “Sauna” or “Protein drink flatrate”.
The types and the options are added gym-wide in the member overview by the managers. Once these are saved, they can be used when adding or editing a contract to a specific user.
## E-Mails[](https://wger.readthedocs.io/en/latest/administration/gym.html#e-mails "Link to this heading")
You can send a batch e-mail to all members of a gym. Currently, there is no support for filtering members based on specific criterion.
How to send e-mails:
  1. Navigate to the gym’s overview and click “Add” on the Email actions button.
  2. Fill in the subject and the body.
  3. Review, and accept the e-mail’s preview.
  4. After submitting, emails will be delivered in batch format based on your cron jobs configuration.


## Configuration[](https://wger.readthedocs.io/en/latest/administration/gym.html#configuration "Link to this heading")
### Inactive members[](https://wger.readthedocs.io/en/latest/administration/gym.html#inactive-members "Link to this heading")
Inactive members are members that have not logged in for X weeks. For example, a trainer can check to see which users have not visited the gym in X weeks.
This can be configured in the following ways:

**Number of Weeks**

The value in weeks after which users are considered inactive (default is 8). This applies to the whole gym and can be deactivated by entering a 0.

**Trainer Configuration**

Each trainer can opt-out of receiving such emails.

**User Configuration**

Individual users can be opt-out of being included in the reminder emails if they don’t want to use the log for any other reason.
### Gym name in the header[](https://wger.readthedocs.io/en/latest/administration/gym.html#gym-name-in-the-header "Link to this heading")
A checkbox to control whether the gym’s name will appear in the header instead of the application’s name for all logged-in users of this gym. This applies to members, trainers, and managers
[](https://wger.readthedocs.io/en/latest/administration/auth_proxy.html "Authentication Proxy \(SSO\)") [Next ](https://wger.readthedocs.io/en/latest/api/api.html "Using the API")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
