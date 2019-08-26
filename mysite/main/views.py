from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")