from django.db import models
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# from accounts.models import CustomUser

# Create your models here.
class Problem(models.Model):

    problem_type_choices = (
        ('c','Confidential'),
        ('sc','Semi-confidential'),
        ('p','Public')
    )

    problem_category_choices = (
        ('agriculture','Agriculture'),
        ('computer_science','Computer Science'),
        ('social_studies','Social Studies'),
        ('environment','Environmental Science'),
        ('mathematics','Mathematics'),
        ('engineering','Engineering'),
        ('physics','physics'),
        ('chemistry','chemistry'),
        ('other','Other')
    )

    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    problem_category = models.CharField(choices=problem_category_choices, max_length=50, default='other', verbose_name="Category of the problem")
    problem_brief = models.TextField()
    # problem_description = models.TextField(verbose_name='Problem complete description ')
    problem_reward = models.IntegerField(verbose_name='Prize money for providing the solution ')
    problem_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def approve_solutions(self):
    #     return self.solutions.filter(approved_solution = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("problems:problem_detail", kwargs={"pk": self.pk})


class Solution(models.Model):
    problem = models.ForeignKey('problems.Problem', related_name='solutions', on_delete=models.CASCADE) # this line connects each solution to an actual problem
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    solution_title = models.CharField(max_length=50, verbose_name="Solution title")
    solution_brief = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_solution = models.BooleanField(default=False)
    rejected_solution = models.BooleanField(default=False)

    def approve(self):
        self.approved_solution = True
        self.save()

    def reject(self):
        self.rejected_solution = True
        self.save()

    class Meta:
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    def __str__(self):
        return self.solution_title

    def get_absolute_url(self):
        return reverse("problems:solution_detail", kwargs={"pk": self.pk})
