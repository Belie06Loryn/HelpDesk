# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def page(request):
    return render(request,'all-pages/index.html',{})

def learn(request):
    return render(request,'all-pages/learn.html',{})  

def profile(request):
    return render(request,'all-pages/profile.html',{})       