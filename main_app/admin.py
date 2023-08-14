from django.contrib import admin
from .models import Knife, Sharpening, Accessory

# Register your models here.
admin.site.register(Knife)
admin.site.register(Sharpening)
admin.site.register(Accessory)