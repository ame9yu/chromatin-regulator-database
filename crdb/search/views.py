from django.shortcuts import render
from django.http import HttpResponse
from .models import chromatin_regulator

# Create your views here.
def index(request):
    cr_result = chromatin_regulator.objects.all()
    context = {'result': cr_result}
    return render(request, "search/index.html",context)

def detail(request, cr_id):
    return HttpResponse("You are at DETAILS")

def download(request):
    return HttpResponse("You are at DOWNLOAD")
