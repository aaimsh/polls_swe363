# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.


@login_required(login_url='/accounts/login/')
def profile(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'profilev2.html', {'user': user})


class UserCreationView(CreateView):
    """If request method is GET it will return a UserCreation Form, if the method is POST, it will process the form,
    validate it, Create an User Instance and save it in the database.
    """
    template_name = 'register.html'
    model = User
    form_class = RegisterForm
    success_url = '/accounts/login/'


class EmailChangeView(UpdateView):
    model = User
    fields = ['email']
    template_name = 'update_email.html'
    success_url = '/accounts/profile/'

    """
    If request method is POST this method will try to get the User Object using get_object_or_404,
    the default method is to to get the kwargs from the url.
    """
    def get_object(self, queryset=None):
        user = get_object_or_404(User, username=self.request.user)
        return user
