from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page3(request):
    return render(request,'page1.html')
def page4(request):
    return render(request,'page2.html')
def second(request):
    return HttpResponse('<h1>VIRAT KOHLI </h1>')