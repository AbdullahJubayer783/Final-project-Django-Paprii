from django.contrib import admin
from .models import FlowerModel
# Register your models here.
class FlowerAdmin(admin.ModelAdmin):
    list_display=['title','quantity','price']
admin.site.register(FlowerModel,FlowerAdmin)