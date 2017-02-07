Django intercooler.js
=====================


Requirements
------------

`Django <https://www.djangoproject.com/>`_ 1.3 or later


Installation
------------

::

    $ pip install django-intercoolerjs


Setup
-----

Just add ``'django.contrib.staticfiles'`` and ``'intercoolerjs'`` to INSTALLED_APPS in
your settings.py::

    INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'intercoolerjs',

        # ...
    )

Refer to Django `static files <https://docs.djangoproject.com/en/dev/howto/static-files/>`_
documentation to configure and deploy static files.


Usage
-----

You use intercooler.js in your Django templates like this::

    {% load static %}
    
    <!-- only if you also need jQuery -->
    <script src="{% static "intercoolerjs/js/jquery.js" %}"></script>
    <!-- this is the minified intercooler.js -->
    <script src="{% static "intercoolerjs/js/intercooler.min.js" %}"></script>
