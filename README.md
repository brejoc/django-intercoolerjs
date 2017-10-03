Django intercooler.js
=====================

django-intercooler.js is just a Django wrapper for [intercooler.js](http://intercoolerjs.org/).

Requirements
------------

[Django](https://www.djangoproject.com/) 1.3 or later


Installation
------------

```bash
$ pip install django-intercoolerjs
```

Setup
-----

Just add `'django.contrib.staticfiles'` and `'intercoolerjs'` to INSTALLED_APPS in
your settings.py
```python
INSTALLED_APPS = (
    # ...

    'django.contrib.staticfiles',
    'intercoolerjs',

    # ...
)
```
Refer to Django [static files](https://docs.djangoproject.com/en/dev/howto/static-files/)
documentation to configure and deploy static files.


Usage
-----

You use intercooler.js in your Django templates like this
```
{% load static %}

<!-- only if you also need jQuery -->
<script src="{% static "intercoolerjs/js/jquery.js" %}"></script>
<!-- this is the minified intercooler.js -->
<script src="{% static "intercoolerjs/js/intercooler.min.js" %}"></script>
```
Since version 1.1.0 of intercooler.js it is also possible to use zepto as an alternative
to jQuery. zepto is not yet bundled with django-intercoolerjs.

Version numbers
---------------

We are keeping the intercooler.js version number, so that intercooler.js releases can
easily be spotted in django-intercoolerjs. But, since we also need a version number, an
other dot number is added.

If intercooler.js version 1.0.3. is the current release, django-intercoolerjs will have
the version number 1.0.3.0. This last number will be incremented with every release of
django-intercoolerjs.

If intercooler.js version 1.0.4 is being released, we keep the last django-intercooler
version number, so that features or bugfixes in django-intercoolerjs can be recognized
easier: 1.0.3.14 ==> 1.0.4.14


Demo
----

A demo project can be found in the `'demo'` folder along with a
README.
