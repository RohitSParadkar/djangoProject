from django.shortcuts import render
from django.http import HttpResponse


def Home (request):
    return render(request,template_name='firstApp/firstAppIndex.html')


def calling (request):
    return HttpResponse("first page")

def aCalling (request):
    return HttpResponse("aCalling")