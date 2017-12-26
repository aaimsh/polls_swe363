from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^create-poll/$', views.create_question_view, name='create-poll'),
    url(r'^$', views.PollsList.as_view(), name='polls-list'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
]

