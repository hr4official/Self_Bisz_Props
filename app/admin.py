from django.contrib import admin
from .models import registartion,subscribe,contact,category
from app.models.category import Category
from app.models.subcat import subcat
from app.models.contact_us import contact
from app.models.portfulio import portfulio
from app.models.registartion import registartion
from app.models.registartion import registartion
from app.models.slider import slider
from app.models.subcategory import subcategory
from app.models.subscribe import subscribe
from app.models.team import team
# Register your models here.

admin.site.register(registartion)
admin.site.register(contact)
admin.site.register(Category)
admin.site.register(portfulio)
admin.site.register(subscribe)
admin.site.register(slider)
admin.site.register(subcat)
admin.site.register(subcategory)
admin.site.register(team)
