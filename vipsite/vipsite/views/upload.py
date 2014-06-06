from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import *
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm
#Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
