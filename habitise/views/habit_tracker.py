from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse

from habitise import models
    
def hello_world(request):
    return HttpResponse('Hello, World!')