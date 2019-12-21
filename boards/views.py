from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import BusinessForm , OwnerForm

def home(request):
  return render(request, 'boards/home.html', {})

def loanapp(request):

  if request.method == 'POST':
    form = BusinessForm(request.POST)
    if form.is_valid():
      form.save()

  form = BusinessForm()
  return render(request,'boards/form.html', {'form': form })

def loanapp2(request):

  if request.method == 'POST':
    form = OwnerForm(request.POST)
    if form.is_valid():
      form.save()

  form = OwnerForm()
  return render(request,'boards/loanapp.html', {'form': form })

def status(request):
  return render(request, 'boards/status.html', {})


