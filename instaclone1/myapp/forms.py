
from django import forms
from models import UserModel


class SignUpForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields = ['phone', 'age', 'full_name', 'gender']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']