import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_mngmt.settings')

app = Celery('inventory_mngmt')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
