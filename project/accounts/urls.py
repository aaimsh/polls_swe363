from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'register/$', views.UserCreationView.as_view(), name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
        name='login'),
    url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url('^password-change-done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^update-password/$', auth_views.PasswordChangeView.as_view(template_name='update_password.html'),
        name='update-password'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^update-email/$', views.EmailChangeView.as_view(), name='update-email'),
]

