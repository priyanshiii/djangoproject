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
    today = datetime.now()
    print (today)
    if request.method == "GET":
        print ('GET REQUEST')
        signup_form = SignUpForm()


    elif request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            full_name = signup_form.cleaned_data['full_name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            print ('%s %s %s %s' % (username, full_name, email, password))
            # saving data to DB
            user = UserModel(full_name=full_name,
                        password=make_password(password),
                        email=email,
                        username=username)
            user.save()

            return render(request, 'success.html', {'name': full_name})
    return render(request, 'index.html', {'today': today, 'signup_form': signup_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = UserModel.objects.filter(username=username).first()

        if user:
            if check_password(password, user.password):
                print ('User is valid')
            else:
                print ('User is invalid')

    elif request.method == 'GET':
        form = LoginForm()

    return render(request, 'login.html', {'form': form})