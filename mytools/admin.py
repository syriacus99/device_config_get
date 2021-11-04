from django.contrib import admin
from mytools.models import Device,DeviceConfiguration,Operator
# Register your models here.
admin.site.register(Device)
admin.site.register(DeviceConfiguration)
admin.site.register(Operator)