import os

from django.conf import settings, global_settings


if not settings.configured:
    # Helper function to extract absolute path
    location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

    settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.admin',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.flatpages',
                'url_tracker',
            ],
            TEMPLATE_CONTEXT_PROCESSORS=(
                "django.contrib.auth.context_processors.auth",
                "django.core.context_processors.request",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                "django.core.context_processors.static",
                "django.contrib.messages.context_processors.messages",
            ),
            TEMPLATE_DIRS=(
                location('templates'),
            ),
            MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES + (
                'url_tracker.middleware.URLChangePermanentRedirectMiddleware',
            ),
            AUTHENTICATION_BACKENDS=(
                'django.contrib.auth.backends.ModelBackend',
            ),
            ROOT_URLCONF='tests.urls',
            DEBUG=False,
            SITE_ID=1,
            APPEND_SLASH=True,
        )
