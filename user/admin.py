from django.contrib import admin
from .models import OrderDetails
# Register your models here.
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['flower_id','title','order_status','date','user_name']
    def user_name(self,obj):
        return obj.user.first_name
    def save_model(self , request , obj , form , change):
        obj.save()
        if obj.order_status == "Complited":
            email_subject = "Complite Order"
            email_body = render_to_string('complite.html',{'none' : 'none'})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
admin.site.register(OrderDetails,OrderDetailsAdmin)