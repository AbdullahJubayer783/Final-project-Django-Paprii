from django.contrib import admin
from . import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('color',)}
    list_display =['color', 'slug']
admin.site.register(models.CategorysModel, CategoryAdmin)