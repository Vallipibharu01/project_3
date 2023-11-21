from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kgf(request):
    return render(request,'kgf.html')

def googly(request):
    return HttpResponse('<h1>Googly is Yashs film</h1>')
