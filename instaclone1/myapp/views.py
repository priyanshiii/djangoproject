# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from forms import SignUpForm
from forms import LoginForm
from django.contrib.auth.hashers import make_password, check_password
from models import UserModel


def signup_view(request):
    if request.method == "GET":
        print ('GET REQUEST')
        today = datetime.now()
        print (today)
        signup_form = SignUpForm()
        return render(request, 'index.html', {'today': today, 'signup_form': signup_form})
    elif request.method == 'POST':
        user_data = SignUpForm(request.POST)
        if user_data.is_valid():
            username = user_data.cleaned_data['username']
            full_name = user_data.cleaned_data['full_name']
            email = user_data.cleaned_data['email']
            password = user_data.cleaned_data['password']
            print ('%s %s %s %s' % (username, full_name, email, password))
            # saving data to DB
            user = UserModel(full_name=full_name,
                        password=make_password(password),
                        email=email,
                        username=username)
            user.save()

            return render(request, 'success.html', {'name': full_name})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = UserModel.objects.filter(username=username).first()

        UserModel.objects.get(id=1)
        if user:
            if check_password(password, user.password):
                print ('User is valid')
            else:
                print ('User is invalid')

    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'login.html', {'form': form})