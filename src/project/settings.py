import os

import dj_database_url

from framework.config import settings as ds
from framework.dirs import DIR_PROJECT
from framework.dirs import DIR_STATIC
from framework.dirs import DIR_TEMPLATES

SECRET_KEY = ds.SECRET_KEY

DEBUG = ds.MODE_DEBUG

ALLOWED_HOSTS = [
    "tms-z43.herokuapp.com",
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "applications.blog.apps.BlogConfig",
    "applications.task103.apps.Task103Config",
    "applications.task301.apps.Task301Config",
    "applications.task302.apps.Task302Config",
    "applications.task303.apps.Task303Config",
    "applications.task304.apps.Task304Config",
    "applications.task305.apps.Task305Config",
    "applications.task306.apps.Task306Config",
    "applications.task307.apps.Task307Config",
    "applications.task309.apps.Task309Config",
    "applications.task310.apps.Task310Config",
    "applications.task311.apps.Task311Config",
    "applications.task402.apps.Task402Config",
]

MIDDLEWARE_RANK = {
    1000: "django.middleware.security.SecurityMiddleware",
    2000: "django.contrib.sessions.middleware.SessionMiddleware",
    3000: "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    4000: "django.contrib.auth.middleware.AuthenticationMiddleware",
    5000: "django.contrib.messages.middleware.MessageMiddleware",
    6000: "django.middleware.clickjacking.XFrameOptionsMiddleware",
}

if not DEBUG:
    MIDDLEWARE_RANK[1500] = "whitenoise.middleware.WhiteNoiseMiddleware"

MIDDLEWARE = [mw for rank, mw in sorted(MIDDLEWARE_RANK.items())]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [DIR_PROJECT / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"

database_url = os.getenv("DATABASE_URL", ds.DATABASE_URL)

DATABASES = {
    "default": dj_database_url.parse(database_url),
}

AUTH_PASSWORD_VALIDATORS = (
    [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
    if not DEBUG
    else []
)

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# static storage settings
STATIC_ROOT = DIR_STATIC.resolve().as_posix()

STATIC_URL = "/static/"
if not DEBUG:
    STATICFILES_STORAGE = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
    )

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
