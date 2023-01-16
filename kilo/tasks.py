import datetime
from shop.celery import app
from . import models


@app.task
def delete_file():
    for file in models.FileUser.objects.filter(created__lte = datetime.datetime.now() - datetime.timedelta(minutes=30)):
        file.delete()
