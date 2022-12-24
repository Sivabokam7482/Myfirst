from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def person1(request):
    return HttpResponse('<h1>This is belongs to work </h1>')

def person2(request):
    return HttpResponse('<i><marquee><b>He will go to America</b></marquee></i>')
    