# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.timezone import now
import datetime

from django.contrib.auth import logout
from django.http import HttpResponseRedirect



def home(request):
    today = datetime.date.today()
    return render(request, "squashire/index.html",
        {'today': today, 'now': now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')
