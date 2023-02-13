from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
# Create your views here.
def index(request):
     return render(request,'home/index.html')
def contact(request):
     return render(request,'home/contact.html')
def error(request,*args, **kwargs):
     return render(request,'home/error.html')
def register(request):
     form = RegistrationForm()
     if request.method == "POST":
         form = RegistrationForm(request.POST)
         if form.is_valid():
            return HttpResponseRedirect('/')
     return render(request,'home/register.html',{'form':form})