from django.shortcuts import render , redirect
from django.views.generic import DetailView
from . import models
from .models import FlowerModel
from user.models import OrderDetails
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.
class DetailsView(DetailView):
    model = models.FlowerModel
    template_name = 'details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'flower'


def buy_now(request, id):
    flower = models.FlowerModel.objects.get(pk=id)
    if flower.quantity > 0:
            history = OrderDetails(flower_id = flower.id,title=flower.title, category=flower.category.color, quantity=1, user=request.user)
            history.save()
            flower.quantity -= 1
            flower.save()
            email_subject = "Placing Order"
            email_body = render_to_string('order_email.html',{'title' : flower.title})
            email = EmailMultiAlternatives(email_subject,'',to=[request.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
    return redirect('profile')    