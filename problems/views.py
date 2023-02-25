from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from problems.models import Problem


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


#########################################################################################33

@login_required
def problem_publish(request,pk):
    problem = get_object_or_404(Problem, pk=pk)
    problem.publish()
    return redirect('problems:problem_detail', pk = pk)

