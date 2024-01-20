from typing import Any
from django.shortcuts import render , redirect
from django.views.generic import ListView
from flower.models import FlowerModel
from catagory.models import CategorysModel
from user.models import OrderDetails
from django.views.generic import UpdateView
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = FlowerModel

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = CategorysModel.objects.get(slug = category_slug)
            return FlowerModel.objects.filter(category=category)
        return FlowerModel.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategorysModel.objects.all()
        # context['objects'] = BorrowBookModel.objects.all()
        return context 
    
class AdminDashboard(ListView):
    template_name = 'dashboard.html'
    model = OrderDetails
    def get_queryset(self):
        return OrderDetails.objects.all()
    


def OrderComplitedView(request,id):
    order = OrderDetails.objects.filter(id=id).first()
    order.order_status = "Completed"
    order.save()
    email_subject = "Complite Order"
    email_body = render_to_string('complite.html',{'none' : 'none'})
    email = EmailMultiAlternatives(email_subject,'',to=[order.user.email])
    email.attach_alternative(email_body,"text/html")
    email.send()
    print(order)
    return redirect('dashboard')
    