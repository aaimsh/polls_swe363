# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.

class UserCreationView(CreateView):
    """If request method is GET it will return a UserCreation Form, if the method is POST, it will process the form,
    validate it, Create an User Instance and save it in the database.
    """
    model = User
    form_class = RegisterForm
    success_url = '/accounts/login/'
