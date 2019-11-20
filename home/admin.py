from django.contrib import admin
from .models import Promotion,Event

# Register your models here.
admin.site.register(Event)
admin.site.register(Promotion)