django-url-tracker
==================

The ``django-url-tracker`` is meant to be a easy-to-use addition to
a website to enhance its SEO. This might seem slightly pointless
as `Cool URIs don't change
<http://www.w3.org/Provider/Style/URI.html>`_. I don't want to argue
with that and not changing URL should be the primary goal. In case,
a URL is changed for some reason, however, this can reflect badly in
terms of SEO as search engines do not appreciate ending up on a 404
page when crawling a known URL. To handle these situations nicely
``django-url-tracker`` keeps track of URL changes and when the *old*
URL is called provides a permanent redirect (HTTP 301) or a gone
response (HTTP 410) for deleted URLs.

The tracking is aimed at those URLs that are generated based on
model fields, e.g. a *slug* field. To start tracking URL changes
for a particular model, you simply have to register the model
with ``url_tracker`` and everytime a model is changed or deleted,
URL changes are recorded.

The HTTP repsonses that provide an ``HttpResponsePremanentRedirect``
or ``HttpResponseGone`` are handled similar to the ``flatpages``
middleware, intercepting ``404`` exceptions and checking for the
requested URLs in all existing ``URLChangeRecords``. Depending
on the recorded data the corresponding HTTP response is return or
a ``404`` is raised when no URL matching the requested one can be
found.

Installation
------------

Installation is as easy as::

    pip install django-url-tracker

Done!

Configuration
-------------

To start using ``url_tracker`` in your project. Just add the
following two lines to your ``settings.py``:

1. Add the middleware ``url_tracker.middleware.URLChangePermanentRedirectMiddleware``
   to the end of  ``MIDDLEWARE_CLASSES`` which should look similar
   to this afterwards::

        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
            'url_tracker.middleware.URLChangePermanentRedirectMiddleware',
        )

2. Add ``url_tracker`` to your ``INSTALLED_APPS`` ::

       INSTALLED_APPS = (
            "url_tracker",
       )



Now you are able to use ``url_tracker`` within you project. All that
remains to do is registering a model for tracking.

Tracking A Model
----------------

This is just a simple example of how to track a model. Let's assume we
have a model ``Project`` that hold details on this particular project and
is made available at the URL ``http://www.example.com/project/some-project/``.
The project's URL is based on the ``SlugField`` of our model. The model could
look like this::

    class Project(models.Model):
        name = models.CharField(max_length=20)
        slug = models.SlugField(max_length=20)
        description = models.CharField(max_length=500)


I will not go into details of how to create the slug as I think this is
common practise. So for now we just assume that ``slug`` is populated
automatically from ``name``. One other thing, however, is required for
the tracker to work, the ``get_absolute_url`` method. Let's add this to
the model::

    class Project(models.Model):
        ...

        @models.permalink
        def get_absolute_url(self):
            return ('project-detail', (), {'slug': self.slug})

And now the missing link to actually start tracking URL changes is adding
the following command to the bottom of the class definition, or the file
for that matter::

    import url_tracker
    url_tracker.track_url_changes_for_model(Project)

You are done. If you go to the admin interface, create a new project
and then change its slug (which changes its URL) you will see a new
``URLChangeRecord`` reflecting the change. Opening the ``old_url`` should
then redirect you to the ``new_url``.

Contributing
------------

If you find issues or would like to see a feature suppored, head over to
the `issues section:
<https://github.com/tangentlabs/django-url-tracker/issues>`_ and report it.

To contribute code in any form, fork the `github repository:
<https://github.com/tangentlabs/django-url-tracker>`_ and clone it locally.
Create a new branch for your feature::

    git commit -b feature/whatever-you-like

push the finished feature to github and open a pull request form the branch.
