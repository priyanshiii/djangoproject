
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime
from forms import SignUpForm
from forms import LoginForm
from forms import PostForm
from django.contrib.auth.hashers import make_password, check_password
from models import UserModel, SessionToken, Post
from imgurpython import ImgurClient


def signup_view(request):
    if request.method == "GET":
        print ('GET REQUEST')
        today = datetime.now()
        print (today)
        signup_form = SignUpForm()
        return render(request, 'index.html', {'today': today, 'signup_form': signup_form})
    elif request.method == 'POST':
            user_data = SignUpForm(request.POST)
            # print 'success'
            if user_data.is_valid():
                username = user_data.cleaned_data['username']
                name = user_data.cleaned_data['name']
                email = user_data.cleaned_data['email']
                password = user_data.cleaned_data['password']
                print ('%s %s %s %s' % (username, name, email, password))
                # saving data to DB
                user = UserModel(name=name,
                                password=make_password(password),
                                email=email,
                                username=username)
                # print 'success'
                user.save()

                return render(request, 'success.html', {'name': name})
            else:
                return render(request, 'index.html')


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

    return render(request, 'login.html')


def feed_view(request):
    user = check_validation(request)
    if user:
        posts = Post.objects.all().order_by('created_on')
        return render(request, 'feed.html', {})
    else:
        return redirect('/login/')


def post_view(request):
    user = check_validation(request)
    if user:
        if request.method == "GET":
            form = PostForm()

            return render(request, 'post.html', {'form': form})
        elif request.method == 'POST':

            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                post = Post(user=user, image=image, caption=caption)
                from django.settings import BASE_DIR
                post.save()
                path = str(BASE_DIR + "/" + post.image.url)
                client = ImgurClient('411f839825bafbc', 'bfcf39279eaa9eca2a8d5d55ba393192b89ea7dd')
                post.image_url = client.upload_from_path(path, anon=True)['link']
                post.save()

    else:
        return redirect('/login/')


def check_validation(request):
  if request.COOKIES.get('session_token'):
    session = SessionToken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
    if session:
        return session.user
  else:
        return None