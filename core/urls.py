from unicodedata import name
from .  import views
from django.urls import path
# from .views import SpAce as uu


urlpatterns =[
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_form, name='signup'),
    path('company/', views.comp, name='company'),
  
]
