from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def Blog(request):
    return render(request, 'blogs/blog.html', {})
    