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

    account_type_choices = (
        ('o','Organization'),
        ('i','Individual')
        )  
    
    user_type = models.CharField(max_length=5, choices=user_type_choices, default='pp', verbose_name="Who you are? ")
    account_type = models.CharField(max_length=5, choices= account_type_choices, default='o', verbose_name="Account Type ")
    email = models.EmailField(max_length=50, unique=True, blank=False, verbose_name="Your Email ")
    is_active = models.BooleanField(default=True) # anyone who signs up for thsi application is by default an active user   
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) # the person who has highest level of control over database

    # need to specify manager class for this user
    objects = CustomUserManager()

    # we are not placing password field here because the password field will always be required
    REQUIRED_FIELDS = ['user_type', 'account_type']

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'


# class User(auth.models.User, auth.models.PermissionsMixin):

#     def __str__(self):
#         return "@{}".format(self.username)

    # def get_absolute_url(self):
    #     return reverse("Solver_detail", kwargs={"pk": self.pk})

