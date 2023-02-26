from django.contrib import admin
from accounts.models import CustomUser, ProblemProvider, ProblemSolver

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ProblemSolver)
admin.site.register(ProblemProvider)
