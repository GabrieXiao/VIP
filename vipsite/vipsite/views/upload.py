from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import *
from django import forms
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response
#Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

import string
import random

import os

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def upload(request):
    msg = "Hello! "
    if request.method == 'POST':
            upload_file = request.FILES['data']
            uploadDir = settings.MEDIA_ROOT

            #Only do this if website is face to public
            #while True:
            #    new_id = id_generator()
            #    if not os.path.isfile(uploadDir + "/" + new_id):
            #        break

            filename = str(upload_file)
            dest = open(uploadDir + "/" + filename , "wb+")
            for chunk in upload_file.chunks():
                dest.write(chunk)
            dest.close()
            msg = "Upload OK"

    return render_to_response('upload.html', {'msg': msg})
