from unicodedata import name
from .  import views
from django.urls import path
# from .views import SpAce as uu


urlpatterns =[
   path('nlogsss', views.Blog, name='space'),
]
