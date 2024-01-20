
from django.urls import path , include
from .views import HomePageView,AdminDashboard,OrderComplitedView
from . import views
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('catagories/<slug:category_slug>/', HomePageView.as_view() , name="category_slug_options"),
    path('post/',include("flower.urls")),
    path('dashboard/',AdminDashboard.as_view(),name="dashboard"),
    path('order_complited/<int:id>',OrderComplitedView,name="order_complited"),
]