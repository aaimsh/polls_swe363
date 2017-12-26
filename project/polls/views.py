# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Question, Choice
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, get_list_or_404
from .forms import CreateQuestionForm, ChoiceForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PollsList(ListView):
    model = Question
    template_name = 'polls_dummy.html'
    context_object_name = 'polls'

    def get_queryset(self):
        return Question.objects.filter(author=self.request.user.username)


class PollDetailView(LoginRequiredMixin, DetailView):
    model = Question
    context_object_name = 'poll'


@login_required()
def create_question_view(request):

    if request.method == 'POST':
        qform = CreateQuestionForm(request.POST)
        qform.question = request.POST['question']
        qform.author = request.user.username

        cform = ChoiceForm(request.POST)
        cform.choice1 = request.POST['choice1']
        cform.choice2 = request.POST['choice2']
        cform.choice3 = request.POST['choice3']
        cform.choice4 = request.POST['choice4']

        if qform.is_valid() and cform.is_valid():
            q = qform.save()
            cform.question = Question.objects.get(pk=q.id)
            cform.save()
            return redirect('/polls/polls-list')
        else:
            return HttpResponse('Error, please press back and try again.')
    qform = CreateQuestionForm()
    cform = ChoiceForm()
    return render(request, 'create_poll.html', {'cform': cform, 'qform': qform})


def vote(request, pk):
    q = get_object_or_404(Question, pk=pk)
    try:
        ans = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        error = "You didn't select a choice"
        return render(request, 'detail_dummy.html', {'error': error, 'poll': q})
    else:
        ans.vote += 1
        ans.save()
    return HttpResponse('Thanks for voting!')

