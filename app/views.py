from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponseNotFound

def index(request):
    print('index')
    return render(request,'index.html')

def next(request):
    print('next')
    return TemplateResponse(request, "next.html")

def exp(request):
    print('exp')
    raise HttpResponseNotFound(request)