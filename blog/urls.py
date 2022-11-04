from unicodedata import name
from .  import views
from django.urls import path
# from .views import SpAce as uu


urlpatterns =[
   path('blog/', views.Blog, name='blog'),
]
