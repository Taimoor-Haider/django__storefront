from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def calculate():
    x = 1
    y = 2
    return x


def index(request):
    x = calculate()
    return render(request, 'hello.html')
