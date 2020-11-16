from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from vacancy.models import Vacancy


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class MyProfileView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class HomeView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, "home.html", {'user': request.user})
