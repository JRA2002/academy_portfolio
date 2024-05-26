from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('profile/',views.ProfileView.as_view(),name='profile')
    
]