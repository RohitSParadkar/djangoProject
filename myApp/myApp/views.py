
from django.http import HttpResponse
from django.shortcuts import render

# def myrequest (request):
#     return HttpResponse("first page")

def myrequest (request):
    return render(request,template_name="index.html")