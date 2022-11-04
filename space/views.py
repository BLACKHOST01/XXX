from django.shortcuts import render
from urllib.request import Request

# Create your views here.
def space_home(request):
    return render(request, 'space/space_home.html', {})
