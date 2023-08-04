from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')
