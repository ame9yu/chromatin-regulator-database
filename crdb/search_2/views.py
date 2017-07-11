# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

def home(request):
    return render(request, "home.html")
