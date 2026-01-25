# water/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'water/index.html')

def remainder(request):
    # You can use a different template if needed
    return render(request, 'water/remainder.html')
