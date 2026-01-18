from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def remainder(request):
    return render(request,'water/index.html')