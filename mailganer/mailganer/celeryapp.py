from __future__ import absolute_import

import os

from celery import Celery
from django.apps import apps

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'mailganer.settings'
)
app = Celery('mailganer')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
