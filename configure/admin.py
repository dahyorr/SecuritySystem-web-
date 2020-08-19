from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.RfidId)
admin.site.register(models.Lockstate)
admin.site.register(models.Gui)
admin.site.register(models.Armstate)
admin.site.register(models.Pincode)
