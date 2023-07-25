from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page5(request):
    return render(request,'page5.html')
def page6(request):
    return render(request,'page6.html')
def third(request):
    return HttpResponse('<h1><center>INDIAN CRICKET TEAM.......</center></h1>')