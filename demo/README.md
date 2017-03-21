# Using intercooler.js with Django

This is a very, very simple demo of how you can use intercooler.js in Django. After you've set up this demo, you'll see a page with a counter that can be incremented.

There are some special things about this:

1. AJAX is used to replace the counter value. The page isn't (re)loaded entirely.
* Not a single line of Javascript is needed, only declarative HTML attributes are used.
* There is no need for a special template or partial for the AJAX repsonse. intercooler.js can also handle this usecase.

# Setup

```Bash
virtualenv env
. ./env/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Now you can visit `http://localhost:8000`.

# Project Structure

The structure of the demo project looks like this:

```
$ tree -L 1
demo
├── README.md
├── counter
├── demo
├── manage.py
├── requirements.txt
└── templates
```

`demo` is the name of the *Django project*. That's why there is also a second `demo` folder in the project, which is part of the basic Django setup. The view and model can be found in the folder `counter`. There you'll find the `index` view in [`views.py`](https://github.com/brejoc/django-intercoolerjs/blob/master/demo/counter/views.py) which handles all the requests. [`models.py`](https://github.com/brejoc/django-intercoolerjs/blob/master/demo/counter/models.py) hosts the `Counter` model which writes our counter value to the database. The `templates` folder contains the only template named [`index.html`](https://github.com/brejoc/django-intercoolerjs/blob/master/demo/templates/index.html), which might be the most interesting part of this demo. Please keep in mind that this is just very simple setup and not neccesarily the best solution.
