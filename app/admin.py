from django.contrib import admin
from .models import registartion,login,forgot,subscribe,contact
# Register your models here.

admin.site.register(registartion)
admin.site.register(login)
admin.site.register(forgot)
admin.site.register(subscribe)
admin.site.register(contact)
