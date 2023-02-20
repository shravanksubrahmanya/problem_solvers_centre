from django.db import models
from django.contrib import auth
from django.urls import reverse
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


# class User(auth.models.User, auth.models.PermissionsMixin):

#     def __str__(self):
#         return "@{}".format(self.username)

    # def get_absolute_url(self):
    #     return reverse("Solver_detail", kwargs={"pk": self.pk})


'''
Problem solver details
'''
# class ProblemSolverIndividual(models.Model):
#     id_card_type_choices = (
#         ('dl', 'Driving License'),
#         ('adhaar', 'Adhaar Card'),
#         ('passport', 'Passport'),
#     )

#     username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, unique=True)
#     first_name = models.CharField(max_length=50, blank=True, verbose_name='Firstname ')
#     last_name = models.CharField(max_length=50, blank=True, verbose_name='Lastname ')
#     id_card_type = models.CharField(max_length=50, choices=id_card_type_choices, default='adhaar', verbose_name= "Personal identity proof type ")
#     id_card_number = models.CharField(max_length=10, verbose_name='Personal identity card number ')
#     adrress = models.CharField(max_length=200, verbose_name="Address ")
#     pin_code = models.IntegerField(max_length=6, verbose_name="Pin Code ")
#     ph_no = models.PhoneNumberField(max_length= 10, verbose_name="Phone Number ")


#     def __str__(self):
#         return self.username

#     # def get_absolute_url(self):
#     #     return reverse("ProblemSolverIndividual_detail", kwargs={"pk": self.pk})
