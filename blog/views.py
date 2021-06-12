from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  return render(request, 'homepage.html')
  #return HttpResponse('Homepage')

def about(request):
  #return HttpResponse('<h1>Hello Isaac</h1>')
  return render(request, 'about.html')