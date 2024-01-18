
from django.urls import path , include
from .views import HomePageView
from . import views
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('catagories/<slug:category_slug>/', HomePageView.as_view() , name="category_slug_options"),
    path('post/',include("flower.urls")),
]