from django.urls import path
from problems import views

app_name = "problems"

urlpatterns = [
    # path("", views.ProblemsView.as_view(), name="problems_home"),
    path("", views.ProblemListView.as_view(), name="problem_list"),
    path("problem/<int:pk>", views.ProblemDetailView.as_view(), name="problem_detail"),

    path("problem/<int:pk>/publish/", views.problem_publish, name="problem_publish"),
]
