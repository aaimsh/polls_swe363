from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'register/$', views.UserCreationView.as_view(template_name='register.html'), name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
