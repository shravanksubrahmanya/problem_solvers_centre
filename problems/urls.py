from django.urls import path
from problems import views

app_name = "problems"

urlpatterns = [
    # path("", views.ProblemsView.as_view(), name="problems_home"),
    path("", views.ProblemListView.as_view(), name="problem_list"),
    path("problem/<int:pk>", views.ProblemDetailView.as_view(), name="problem_detail"),
    path("problem/new", views.ProblemCreateView.as_view(), name="problem_new"),
    path("drafts/", views.DraftListView.as_view(), name="problem_draft_list"),
    path("problem/<int:pk>/publish/", views.problem_publish, name="problem_publish"),
    path("problem/<int:pk>/edit", views.ProblemUpdateView.as_view(), name="problem_edit"),
    path("problem/<int:pk>/remove", views.ProblemDeleteView.as_view(), name="problem_remove"),
]
