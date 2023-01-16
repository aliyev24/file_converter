from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('document',)


@admin.register(models.FileUser)
class FileUserAdmin(admin.ModelAdmin):
    list_display = ('id',)
