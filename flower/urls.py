from django.urls import path , include

from . import views
urlpatterns = [
    path('details/<int:id>',views.DetailsView.as_view(),name="details_flower"),
    path('buy/<int:id>',views.buy_now,name="buy_flower"),
    
]