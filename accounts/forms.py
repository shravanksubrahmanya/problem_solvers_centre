# from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        fields = ('user_type','username','email', 'password1', 'password2')
        model = CustomUser # no braces here since a model is not callable

    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
