from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Nivi(request):
    return HttpResponse('<h2><marquee><i>Nivi is Good Girl</i></marquee></h2>')

def siva(request):
    return HttpResponse('<h1>Vannakam,Enna Thambi</h1>')
    