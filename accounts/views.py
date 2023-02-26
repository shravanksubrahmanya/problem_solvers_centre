from accounts.forms import SignUpForm, ProblemSolverForm, ProblemProviderForm
from .managers import CustomUserManager
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import CustomUser, ProblemProvider, ProblemSolver

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProblemProviderDetailView(DetailView, LoginRequiredMixin):
    model = ProblemProvider
    template_name = "accounts/problem_provider_detail.html"
    login_url = 'login/'
    redirect_field_name = 'index.html'

class ProblemSolverDetailView(DetailView, LoginRequiredMixin):
    model = ProblemSolver
    template_name = "accounts/problem_solver_detail.html"
    login_url = 'login/'
    redirect_field_name = 'index.html'


class ProblemSolverUpdateView(UpdateView, LoginRequiredMixin):
    model = ProblemSolver
    template_name = "accounts/problem_solver_form.html"
    login_url = 'login'
    redirect_field_name = 'accounts/problem_solver_account.html'
    form_class = ProblemSolverForm

class ProblemProviderUpdateView(UpdateView, LoginRequiredMixin):
    model = ProblemProvider
    template_name = "accounts/problem_provider_form.html"
    login_url = 'login/'
    redirect_field_name = 'accounts/problem_provider_account.html'
    form_class = ProblemProviderForm


###################################################33
