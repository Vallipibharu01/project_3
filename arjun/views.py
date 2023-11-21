from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def pushpa(request):
    return render(request,'pushpa.html')

def arya(reques):
    return HttpResponse('<marquee><h1> Arya is Allu Arjuns film </h1></marquee>')