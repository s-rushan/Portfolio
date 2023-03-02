from django.shortcuts import render,redirect
from datetime import datetime
from webpages.models import contact
from django.contrib import messages
from django.http import HttpResponse,FileResponse
from wsgiref.util import FileWrapper
from django.db import connection
import os
from django.views.generic import View
# Create your views here.

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def form(request):
    return redirect(form)

def index(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact_view(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        Contact=contact(email=email, name=name, subject=subject, message=message, date=datetime.today())
        Contact.save()
        messages.success(request,'Form Submit Succesfully')
    return render(request, 'contact.html')

class downloadpdf(View):
    def get(self, request,file_path):
        # file_path="static/assets/img/test.txt"
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + file_name
            return response

def mdetail(request):
    return render(request,'portfolio-details.html')

# def downloadpdf(request):
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     filename = "test.txt"
#     filepath=base_dir+'/files/' +filename
#     filename = os.path.basename(thefile)
#     chunk_size = 8192
#     response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
#     response['content-length'] = os.path.getsize(thefile)
#     response['content-disposition'] = "Attachment;filename=%s"%filename
#     return response