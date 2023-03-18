# Quick-start development settings - unsuitable for .production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
import sys
from datetime import timedelta
from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "apps"

sys.path.append(str(APPS_DIR))

# Read .env file is exists
env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", False)
TIME_ZONE = 'UTC'
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = False
USE_TZ = True
LOCALE_PATHS = [str(BASE_DIR / "locale")]
# ------------------------------------------------------------------------------

# DATABASE
# ------------------------------------------------------------------------------
DATABASES = {
    "default": env.db("DATABASE_URL")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "apps.contrib.sites.migrations"}

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    'rest_framework_simplejwt.token_blacklist',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    # "drf_spectacular",
]

LOCAL_APPS = [
    "authentication",
    # Your stuff: custom apps go here
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
# MIGRATION_MODULES = {"sites": "{{ cookiecutter.project_slug }}.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
AUTH_USER_MODEL = "authentication.User"

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
           str(BASE_DIR / "templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
ADMINS = [("""{{cookiecutter.author_name}}""", "{{cookiecutter.email}}")]
MANAGERS = ADMINS

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(BASE_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_TIMEOUT = 5

# DJANGO_ALLAUTH
# ------------------------------------------------------------------------------
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_ADAPTER = 'apps.accounts.adapters.DefaultAccountAdapter'

REST_USE_JWT = True
REST_SESSION_LOGIN = False
REST_AUTH_PW_RESET_USE_SITES_DOMAIN = True

# REST FRAMEWORK
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    'TEST_REQUEST_RENDERER_CLASSES': ('djangorestframework_camel_case.render.CamelCaseJSONRenderer',),
    'TEST_REQUEST_PARSER_CLASSES': ('djangorestframework_camel_case.parser.CamelCaseJSONParser',),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'apps.authentication.serializers.UserDetailsSerializer'
}
