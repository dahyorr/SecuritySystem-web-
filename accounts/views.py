from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.


class LogIn(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = 'Log In'
        return context


class LogOut(auth_views.LogoutView):
    pass


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    date = datetime.date(datetime.now())
    time = datetime.time(datetime.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_active'] = 'active'
        context['date'] = self.date
        context['time'] = self.time
        return context
