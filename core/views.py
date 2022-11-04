from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html', {})


def login_page(request):
    return render(request, 'auth/login.html')

def signup_form(request):
    return render(request, 'auth/signup.html')

def comp(request):
    return render(request, 'home/company.html', {})


# def SpAce(request):
#     return render(request, 'home/space.html', {})