# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import chromatin_regulators

def home(request):
    return render(request, "home.html")

def result(request):
    return render(request, "result.html")

def download(request):
    all_cr = chromatin_regulators.objects.all()
    return render(request, "download.html", {"cr":all_cr})
