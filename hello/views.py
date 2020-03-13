from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def home(request):
    name = request.GET['name']
    age = request.GET['age']
    getRequestDict = request.GET
    return JsonResponse(getRequestDict)


