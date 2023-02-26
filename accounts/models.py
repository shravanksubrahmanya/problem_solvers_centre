from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.

# for custom user
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Model representation for user'''
    user_type_choices = (
        ('ps','Problem Solver'),
        ('pp','Problem Provider')
        )
    
    user_type = models.CharField(max_length=5, choices=user_type_choices, default='pp', verbose_name="Who you are? ")
    username = models.CharField(max_length=50, verbose_name="Your username ", unique=True)
    email = models.EmailField(max_length=50, unique=True, blank=False, verbose_name="Your Email ")
    is_active = models.BooleanField(default=True) # anyone who signs up for thsi application is by default an active user   
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) # the person who has highest level of control over database

    # need to specify manager class for this user
    objects = CustomUserManager()

    # we are not placing password field here because the password field will always be required
    REQUIRED_FIELDS = ['user_type','email']

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

# to create a ProblemSolver or ProblemProvider object as soon as CustomUser is created
def create_problem_solver_profile(sender, instance, created, **kwargs):
    
    if created:
        if instance.user_type == 'ps':
            ProblemSolver.objects.create(username = instance)
        else:
            ProblemProvider.objects.create(username = instance)
    
post_save.connect(create_problem_solver_profile, sender=CustomUser)

'''
Problem solver details
'''
class ProblemSolver(models.Model):
    id_card_type_choices = (
        ('dl', 'Driving License'),
        ('adhaar', 'Adhaar Card'),
        ('passport', 'Passport'),
    )

    username = models.OneToOneField(CustomUser, related_name="ProblemSolver", verbose_name ="username", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, verbose_name='Firstname ', blank=True)
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Lastname ')
    id_card_type = models.CharField(max_length=50, choices=id_card_type_choices, default='adhaar', verbose_name= "Personal identity proof type ")
    id_card_number = models.CharField(max_length=10, verbose_name='Personal identity card number ', blank=True)
    address = models.CharField(max_length=200, verbose_name="Address ", blank=True)
    pin_code = models.CharField(max_length=6, verbose_name="Pin Code ", blank=True)
    ph_no = models.CharField(max_length=10, verbose_name="Phone Number ", blank=True)
    personal_description = models.TextField(blank=True)

    def fullname(self):
        return self.first_name + " " + self.last_name
    
    def id_card_details(self):
        return self.id_card_type + ": "+ self.id_card_number

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("accounts:problem_solver_account", kwargs={"pk": self.pk})


'''
Problem Provider details
'''

class ProblemProvider(models.Model):
    username = models.OneToOneField(CustomUser, related_name="ProblemProvider", verbose_name= "username", on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=50, verbose_name="Organization name", blank=True)
    provider_brief = models.CharField(max_length=1000, verbose_name="Brief description", blank=True)
    govt_liscence_id = models.CharField(max_length=50, verbose_name="Liscence number", blank=True)
    address = models.CharField(max_length=500, verbose_name="Address ", blank=True)
    pin_code = models.CharField(max_length=6, verbose_name="Pin Code ", blank=True)
    ph_no = models.CharField(max_length=10, verbose_name="Phone Number ", blank=True)
    personal_description = models.TextField( blank= True)

    class Meta:
        verbose_name =  "ProblemProvider"
        verbose_name_plural = "ProblemProviders"

    def __str__(self):
        return self.provider_name

    def get_absolute_url(self):
        return reverse("accounts:problem_provider_account", kwargs={"pk": self.pk})
