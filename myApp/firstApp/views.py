from django.shortcuts import render
from django.http import HttpResponse
from .models import details
from django.shortcuts import get_object_or_404


def Home (request):
    detail_list = details.objects.all()
    return render(request,'firstApp/firstAppIndex.html',{'detail_list':detail_list})


def finddetails (request,user_id):
    get_id = get_object_or_404(details,pk = user_id)
    return render(request,'firstApp/firstAppIndex.html',{'get_id':get_id})

def aCalling (request):
    return HttpResponse("aCalling")