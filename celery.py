import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_space_flight.settings")
app = Celery('challenge_by_coodesh.celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# @app.task(bind=True)
# def deb
