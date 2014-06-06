from django.shortcuts import render
#from ecommerce.models import Honey
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import *
from django import forms

def index(request):
    #ps = Honey.objects.all()
    return render(request, 'index.html')
