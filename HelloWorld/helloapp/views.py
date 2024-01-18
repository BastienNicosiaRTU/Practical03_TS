from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    # Return a simple HTML response with CSS and JavaScript
    return render(request, 'hello_world.html')
