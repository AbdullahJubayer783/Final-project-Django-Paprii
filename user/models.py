from django.db import models
from django.contrib.auth.models import User 
ORDER_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
]
class OrderDetails(models.Model):
    flower_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order_status = models.CharField(choices=ORDER_STATUS , default = 'Pending',max_length=15)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='histories', null=True, blank = True)
    date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    def __str__(self) -> str:
        return self.title