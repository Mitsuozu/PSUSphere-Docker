"""Container-only Django settings; original settings.py remains untouched."""
import os
from .settings import *  # noqa: F403,F401

DEBUG = True  # Classroom/local development only
ALLOWED_HOSTS = [host.strip() for host in os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",") if host.strip()]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("SQLITE_PATH", "/data/db.sqlite3"),
    }
}
