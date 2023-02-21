from django.urls import path
from problems import views

app_name = "problems"

urlpatterns = [
    path("", views.ProblemsView.as_view(), name="problems_home"),
]
