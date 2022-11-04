from django.shortcuts import render

# Create your views here.
def parcel(request):
    return render(request, 'parcel/parcel.html', {})
    