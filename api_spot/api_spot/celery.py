import os

from celery import Celery

app_name = "api_spot"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{app_name}.settings")
app = Celery(app_name)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
