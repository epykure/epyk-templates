
![](https://raw.githubusercontent.com/epykure/epyk-templates/master/static/images/logo.ico)

### Epyk templates 

This is a collection of local reports to be run locally to show how to write HTML pages using Epyk core web components.

This repository will group all the tutorial used in the various Jupyter notebook with some extra demo on more complex implementations.

Those reports can used directly on your computer by downloading the project.

Repo Structure
==============


Usage
=====

First install Epyk to your Python environment.

```py
pip install epyk
```

Then run the reports using the generic runner PatchRunner. This will run all the report in the entier repository.

It is possible to only run few reports by changing the below variable.


```py
# To reduce the scope of filters to generate
filter = None # 'data_'
category = None
```

In those reports and during the implementation phases (before releasing the report to a production mode), it is common practice to use
the below line of code to change the icon to a dark one.

This will warn any users that those reports are not yet validated.

```py
page.headers.dev()
```

It is obviously possible to customise this icon but using the below instead

```py
page.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo
```

Those reports are used as Unit Test for the framework so do not hesitate to propose new ones to help on improving the release management.

Please let us know your comments or your experience with the framework.
