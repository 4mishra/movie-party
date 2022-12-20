from pathlib import Path
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-8@=e+3+&po-_t2&huceudi9a#wfqp!$^*%971f@=5_(kw!gqaz"

DEBUG = not os.environ.get("DEBUG")

ALLOWED_HOSTS = [
    ".localhost",
    "testserver",
    "127.0.0.1",
    "movies",
    "[::1]",
    os.environ.get("DEPLOYED_HOST", "localhost"),
]

CORS_ALLOWED_ORIGINS = [
    os.environ.get("CORS_HOST", "http://localhost:3001"),
    os.environ.get("GHI_URL", "http://localhost:3000"),
    os.environ.get("WATCH_PARTIES_URL", "http://localhost:8001"),
    os.environ.get("WATCHLISTS_URL", "http://localhost:8002"),
    f"https://{os.environ.get('DEPLOYED_HOST')}",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    os.environ.get("CORS_HOST", "http://localhost:3001"),
    os.environ.get("GHI_URL", "http://localhost:3000"),
    os.environ.get("WATCH_PARTIES_URL", "http://localhost:8001"),
    os.environ.get("WATCHLISTS_URL", "http://localhost:8002"),
    f"https://{os.environ.get('DEPLOYED_HOST')}",
]

INSTALLED_APPS = [
    "corsheaders",
    "movies_app.apps.MoviesAppConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "movies_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "movies_project.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

DATABASES = {}
DATABASES["default"] = dj_database_url.config()

AUTH_PASSWORD_VALIDATORS = [
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
