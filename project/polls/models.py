# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
