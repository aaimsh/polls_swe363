from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^create-poll/$', views.create_question_view, name='create-poll'),
    url(r'^polls-list/$', views.PollsList.as_view(), name='polls-list'),
    url(r'^poll-detail/(?P<pk>[0-9]+)/$', views.PollDetailView.as_view(template_name='detail_dummy.html'),
        name='poll-detail'),
    url(r'^(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.PollDetailView.as_view(template_name='results.html'), name='results'),

]

