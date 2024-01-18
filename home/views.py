from django.shortcuts import render
from django.views.generic import ListView
from flower.models import FlowerModel
from catagory.models import CategorysModel
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