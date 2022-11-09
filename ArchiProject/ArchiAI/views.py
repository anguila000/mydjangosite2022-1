from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def quad(request):
    # return HttpResponse("Hello world!")
    template = loader.get_template('quad.html')
    return HttpResponse(template.render())

