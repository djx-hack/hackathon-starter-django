from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
	password1 = forms.CharField(
		label=_("Password"),
		strip=False,
		widget=forms.PasswordInput,
		)
	password2 = forms.CharField(
		label=_("Password confirmation"),
		widget=forms.PasswordInput,
		strip=False,
	)
	class Meta:
		model = CustomUser
		fields = ('email', 'password1', 'password2', )