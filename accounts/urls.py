from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view() , name='login'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
]
