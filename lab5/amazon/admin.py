from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.MyUser)
admin.site.register(models.Student)
# register track and intake models 
admin.site.register(models.Track)
admin.site.register(models.Intake)

