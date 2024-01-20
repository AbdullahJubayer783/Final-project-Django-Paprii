
from django.urls import path , include
from .views import UserCreationView , UserLoginView , UserLogoutview , UserProfileView , activate
urlpatterns = [
    path('register/',UserCreationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutview.as_view(),name='logout'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('active/<uid64>/<token>/',activate,name='active'),
]