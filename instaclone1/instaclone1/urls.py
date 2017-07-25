
from django.conf.urls import url
from django.contrib import admin

from myapp.views import signup_view, login_view, post_view, feed_view
urlpatterns = [
  url('post/', post_view),
  url('feed/', feed_view),
  url('login/', login_view),
  url('', signup_view)
]