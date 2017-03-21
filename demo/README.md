# What?

This is a very, very simple demo of how you an use intercooler.js in Django. After you've set up this demo, you'll see a page with a counter that can be incremented.

There are some special things about this:

1. AJAX is used to replace the counter value. The page isn't (re)loaded entirely.
* Not a single line of Javascript is needed, only special intercooler.js HTML attributes.
* No special version of the template or partial for the replacement is needed. Although you can do that if you need it.

# Setup

```Bash
virtualenv env
. ./env/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

Now you can visit `http://localhost:8000`.

