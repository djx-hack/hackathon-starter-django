from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.views.generic import TemplateView


def profile(request):
	return render(request, 'users/profile.html')

def register(request):
	if request.user.is_authenticated:
		return redirect(reverse('index'))
	else:
		if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				return redirect(reverse('index'))
			else:
				return render(request, 'users/register.html', {'form':form})
		else:
			form = CustomUserCreationForm
			return render(request, 'users/register.html', {'form':form})