# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import  datetime
from forms import SignUpForm

def signup_view(request):
    if request.method == "GET":
        today = datetime.now()
        return render(request, 'index.html', {'today': today})
