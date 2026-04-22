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
  * [](https://wger.readthedocs.io/en/latest/api/routines.html)
    * [Days](https://wger.readthedocs.io/en/latest/api/routines.html#days)
    * [](https://wger.readthedocs.io/en/latest/api/routines.html#sets-and-exercises)
      * [Supersets](https://wger.readthedocs.io/en/latest/api/routines.html#supersets)
    * [Weight, sets, repetitions, RiR, etc.](https://wger.readthedocs.io/en/latest/api/routines.html#weight-sets-repetitions-rir-etc)
    * [Using the results](https://wger.readthedocs.io/en/latest/api/routines.html#using-the-results)


All the rest
  * [Contributing](https://wger.readthedocs.io/en/latest/contributing.html)
  * [Changelog](https://wger.readthedocs.io/en/latest/changelog.html)


[wger project](https://wger.readthedocs.io/en/latest/index.html)
  * [](https://wger.readthedocs.io/en/latest/index.html)
  * [Using the API](https://wger.readthedocs.io/en/latest/api/api.html)
  * Using the routine API
  * [ Edit on GitHub](https://github.com/wger-project/docs/blob/master/docs/api/routines.rst)


* * *
# Using the routine API[](https://wger.readthedocs.io/en/latest/api/routines.html#using-the-routine-api "Link to this heading")
This section explains how the data model behind the routines and its different calculations work and is only relevant to you if you plan on using the API directly.
**Endpoint:** `/api/v2/routine/`
**Possible values:**
  * `name`, 50 chars max
  * `description`, optional, 1000 chars max
  * `start date` and `end date`
  * `fit_in_week` flag to indicate that the routine should fit in a week, after the last regular workout day, the remainder of the week is filled with rest days


## Days[](https://wger.readthedocs.io/en/latest/api/routines.html#days "Link to this heading")
**Endpoint:** `/api/v2/day/`
**Possible values:**
  * `type` the type of workout day. These will change the way the workout for a specific day is handled, but currently this setting is ignored. Current values are: * `custom` (default) * `enom` * `amrap` * `hiit` * `tabata` * `edt` * `rft` * `afap`
  * `name`, 50 chars max
  * `description`, optional, 1000 chars max
  * `is_rest` flag indicating that this is a rest day


A day is the building block of a routine. It consists of several linked days that can be configured in different ways.
```
+----------------+      +-----------------+      +-----------------+
|Day 1 - Push    |      |Day 2 - Pull     |      |Day 3 - Legs     |
|----------------+      |-----------------+      |-----------------+
|order=1         | ---> |order=2          | ---> |order=3          |
|rest=false      |      |rest=false       |      |rest=false       |
|needs_logs=true |      |needs_logs=false |      |needs_logs=false |
+----------------+      +-----------------+      +-----------------+

```

The routine will calculate from the list a sequence of days that are planned. This allows you to create very flexible setups. If the routine starts on the 1.1, it will create the following sequence:
1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 | 1.9 | 1.10
---|---|---|---|---|---|---|---|---|---
Day 1 | Day 2 | Day 3 | Day 1 | Day 2 | Day 3 | Day 1 | Day 2 | Day 3 | Day 1
1 | 1 | 1 | 2 | 2 | 2 | 3 | 3 | 3 | 4
An important concept (and parameter) is the “iteration”. An iteration is simply the complete cycle of all the days in the routine. Once all the days in the routine have been completed, the next occurrence of the first day marks the start of a new iteration. Note that in practice, this will most likely be a week.
With the `need_logs_to_advance` flag you can control whether there needs to be a logged session for the day to proceed. Otherwise, the day will be repeated until a log is saved, like in the example below with day 3 where the user logged a session on the 1.8.
1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 | 1.9 | 1.10
---|---|---|---|---|---|---|---|---|---
Day 1 | Day 2 | Day 3 | Day 1 | Day 2 | Day 3 | Day 3 | Day 3 | Day 1 | Day 2
1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 3 | 3
Days marked as “rest” can be used to pad training days and do not contain any exercises.
Here is an example if the `fit_in_week` flag is set for the routine:
1.1 - Monday | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8 - Monday | 1.9 | 1.10
---|---|---|---|---|---|---|---|---|---
Day 1 | Day 2 | Day 3 | null | null | null | null | Day 1 | Day 2 | Day 3
1 | 1 | 1 | null | null | null | null | 2 | 2 | 2
**Labels**
You can group the workout days (such as “Deload week” or similar) by adding labels to the routine. A label accepts the following properties:
  * `start_offset`, the number of days after the start of the routine when this label becomes active
  * `end_offset`, the number of days after the start of the routine when this label ceases being active
  * `label`, the label that will be displayed in the UI


## Sets and exercises[](https://wger.readthedocs.io/en/latest/api/routines.html#sets-and-exercises "Link to this heading")
**Endpoints** `/api/v2/slot/` and `/api/v2/slot-entry/`
**Possible values:**
  * `type` the type of set. These will change the way the set is handled or displayed, but currently this setting is ignored. Current values are: * `normal` (default) * `dropset` * `myo` * `partial` * `forced` * `tut` * `iso` * `jump`
  * `repetition_rounding` and `weight_rounding`: Rounding factor for the respective values. Note that this only applies to that specific slot config, if you want to add a default value you can change the user pofile, which also has these settings and, if set, will be written to the config table _when creating new entries_.


You can add exercises to a slot (set). These slots have a `SlotConfig` entry, and different individual config entries for individual properties where the magic happens.
### Supersets[](https://wger.readthedocs.io/en/latest/api/routines.html#supersets "Link to this heading")
If you add more than one slot entry to a slot, it automatically becomes a superset. The specific order of exercises (in the gym mode only!) is the interleaved list of exercises. Not all exercises need to have the same number of sets, e.g.:
  * Exercise 1, 4 sets
  * Exercise 2, 2 sets
  * Exercise 3, 3 sets


Would result in:
  * Exercise 1
  * Exercise 2
  * Exercise 3
  * Exercise 1
  * Exercise 2
  * Exercise 3
  * Exercise 1
  * Exercise 3
  * Exercise 1


(with the respective values for weight, reps, etc.)
## Weight, sets, repetitions, RiR, etc.[](https://wger.readthedocs.io/en/latest/api/routines.html#weight-sets-repetitions-rir-etc "Link to this heading")
**Endpoints:**
  * `/api/v2/[max-]weight-config/`
  * `/api/v2/[max-]sets-config/`
  * `/api/v2/[max-]repetitions-config/`
  * `/api/v2/[max-]rir-config/`
  * `/api/v2/[max-]rest-config/`


**Possible values:**
  * `iterations`: the iteration this takes effect on.
  * `value`: Decimal number with the wanted value
  * `operation`: Operation to perform: `+`, `-` for adding or subtracting the value, or to replace it `r`
  * `step`: How to calculate the new value: `abs` or `percent`
  * `requirements`: JSON field, see above
  * `repeat`: flag indicating whether this rule should be repeated till a new rule takes effect (this allows you to e.g. increase the weight every week with only one rule)


To configure the specific values for weight, nr of sets, etc. use these endpoints to set the appropriate properties. All of these are optional, in which case they will return null over the API. In this case the number of sets will be set to 1.
You can create progression rules that will happen at specific iterations and either modify the weight (+2kg, -10%) or replace it with a new value (45kg). The value at a specific iteration is the stacked calculated value (unless you just replace the value with a new one) of the previous ones. There are also a handful of possibilities on how to calculate the value such as increasing / decreasing or using an absolute value or a percentage.
The behaviour is the same for all of them, here with a weight config example:
**Iteration** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
---|---|---|---|---|---|---|---|---
**Config** | 50kg | -/- | -/- | +10% | -/- | +2kg | +1kg | 45kg
**Result** | 50kg | 50kg | 50kg | 55kg | 55kg | 57kg | 58kg | 45kg
When exactly an iteration happens depends on how the days are configured, but realistically it’s probably a week long.
You can further control if a value increases by setting the `requirements` field. This field is a JSON object that can currently contains an object with the following keys:
```
{
     "rules": [
        "weight",
        "repetitions",
        "rir",
        "rest"
     ]
}

```

You can add values to “rules” that need to be checked for the rule to apply. Only if all of them are met (i.e., the user logged them in the last iteration), the rule will be applied. For example, if the weight should change from 8x60 to 8x65, depends on the weight and repetitions but the user didn’t log at least that in the last workout, it will stay at 8x60 until they do.
If this is not enough, there is an escape hatch in the form of setting a custom python class that can perform any calculations you might need. Please consider that while this works, it is not currently in use so we would be happy if you got in touch with us.
## Using the results[](https://wger.readthedocs.io/en/latest/api/routines.html#using-the-results "Link to this heading")
Once you have added all your slots and progression rules, you can use the following endpoints to get computed values for each iteration/week:

`/api/v2/routine/{id}/date-sequence-display`

Returns a list of WorkoutDayData objects that contain the calculated values for each day in the routine. This endpoint is used to display the routine in the frontend and does some light grouping of the data.

`/api/v2/routine/{id}/date-sequence-gym`

Returns a list of WorkoutDayData objects to use in the gym. This endpoint returns the data split into individual slots and interleaved in case of supersets as described above.

`/api/v2/routine/{id}/structure`

Returns the raw data structure of the routine, including all the days, slots and slot configs.

`/api/v2/routine/{id}/logs`

Returns all the sessions and logs for the routine.

`/api/v2/routine/{id}/stats`

Returns the stats for the routine, including the total volume, total weight, total reps, etc.
[](https://wger.readthedocs.io/en/latest/api/api.html "Using the API") [Next ](https://wger.readthedocs.io/en/latest/contributing.html "Contributing")
* * *
© Copyright 2025, Roland Geider.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
[**GenAI apps + MongoDB Atlas** You don't need a separate database to start building GenAI-powered apps.](https://server.ethicalads.io/proxy/click/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)
Close Ad
![](https://server.ethicalads.io/proxy/view/10126/019cbbb2-4e9f-76e3-aec8-c147759ded32/)
