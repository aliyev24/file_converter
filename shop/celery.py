import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery("shop")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete_file_after_10minute': {
        'task': 'kilo.tasks.delete_file',
        'schedule': crontab(minute='*/1'), },
}
