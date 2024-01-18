from django.db import models

# Create your models here.
class CategorysModel(models.Model):
    color = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100,unique=True,null=True, blank=True)
    def __str__(self):
        return f'category - {self.color}'