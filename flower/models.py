from django.db import models
from catagory.models import CategorysModel
# Create your models here.
class FlowerModel(models.Model):
    image = models.ImageField(upload_to ='flower/media/uploads/',blank=True, null=True)
    title = models.CharField(max_length=300)
    descriptions = models.TextField()
    quantity = models.IntegerField()
    price = models.CharField(max_length=100,blank=True, null=True)
    category = models.ForeignKey(CategorysModel, on_delete = models.CASCADE)

    def __str__(self) :
        return self.title