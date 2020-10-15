from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile', profile, name='profile'),

    # restrict logged in user from accessing login page
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True),
          name='login'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register', register, name='register'),

    # Password change functionality
    path(
        'password-change-success',
        TemplateView.as_view(template_name='registration/password_change_success.html'),
        name='password_change_success'
    ),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change.html',
            success_url = '/users/password-change-success'
        ),
        name='password_change'
    ),
]
