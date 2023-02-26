from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("problem_solver/<int:pk>", views.ProblemSolverDetailView.as_view(), name="problem_solver_account"),
    path("problem_provider/<int:pk>", views.ProblemProviderDetailView.as_view(), name="problem_provider_account"),
    path("problem_solver/<int:pk>/edit", views.ProblemSolverUpdateView.as_view(), name="problem_solver_edit"),
    path("problem_provider/<int:pk>/edit", views.ProblemProviderUpdateView.as_view(), name="problem_provider_edit"),
]
