from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from problems.models import Problem
from problems.forms import ProblemForm


# Create your views here.
class ProblemsView(TemplateView):
    template_name = "problems_home.html"

class ProblemListView(ListView):
    model = Problem
    template_name = "problem_list.html"

    def get_queryset(self):
        return Problem.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class ProblemDetailView(DetailView):
    model = Problem
    template_name = "problem_detail.html"


class ProblemCreateView(CreateView, LoginRequiredMixin):
    model = Problem
    template_name = "problem_form.html"
    login_url = 'login/'
    redirect_field_name = 'problems/problem_detail.html'
    form_class = ProblemForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DraftListView(ListView, LoginRequiredMixin):
    model = Problem
    template_name = "problem_draft_list.html"
    login_url = 'login/'
    redirect_field_name = 'problems/problem_list.html'
    def get_queryset(self):
        return Problem.objects.filter(published_date__isnull = True).order_by('created_date') # i.e select posts which have published date as null

class ProblemUpdateView(UpdateView, LoginRequiredMixin):
    model = Problem
    template_name = "problem_form.html"
    login_url = 'login/'
    redirect_field_name = 'problems/problem_detail.html'
    form_class = ProblemForm

class ProblemDeleteView(DeleteView):
    model = Problem
    template_name = 'problem_confirm_delete.html'
    success_url = reverse_lazy('problems:problem_list')



#########################################################################################33

# action to publish the created problem
@login_required
def problem_publish(request,pk):
    problem = get_object_or_404(Problem, pk=pk)
    problem.publish()
    return redirect('problems:problem_detail', pk = pk)

