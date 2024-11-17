INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "custom_auth.apps.CustomAuthConfig",
    "car.apps.CarConfig",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    INSTALLED_APPS.append("debug_toolbar_force")
