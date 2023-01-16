from django.db import models


class File(models.Model):
    document = models.FileField(upload_to='photos/%Y/%m/%d/')


class FileUser(models.Model):
    documentUser = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
