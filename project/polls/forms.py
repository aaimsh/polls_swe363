from django import forms
from .models import Question, Choice


class CreateQuestionForm(forms.Form):
    author = None
    question = forms.CharField(max_length=150)

    def save(self):
        q = Question()
        q.author = self.author
        q.question = self.question
        q.save()
        return q


class ChoiceForm(forms.Form):
    question = None
    choice1 = forms.CharField(max_length=100)
    choice2 = forms.CharField(max_length=100)
    choice3 = forms.CharField(max_length=100)
    choice4 = forms.CharField(max_length=100)

    def save(self):
        c1 = Choice()
        c2 = Choice()
        c3 = Choice()
        c4 = Choice()
        c1.choice = self.choice1
        c2.choice = self.choice2
        c3.choice = self.choice3
        c4.choice = self.choice4
        c1.question = self.question
        c2.question = self.question
        c3.question = self.question
        c4.question = self.question
        c1.save()
        c2.save()
        c3.save()
        c4.save()
