# from django.contrib.auth import get_user_model
from accounts.models import CustomUser, ProblemProvider, ProblemSolver
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        fields = ('user_type','username','email', 'password1', 'password2')
        model = CustomUser # no braces here since a model is not callable

    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)

class ProblemSolverForm(forms.ModelForm):
    
    class Meta:
        model = ProblemSolver
        fields = ("first_name","last_name","id_card_type","id_card_number","address","pin_code","ph_no","personal_description")

        widgets = {
            'first_name' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'last_name' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'id_card_type' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'id_card_number' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'address': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea address-field'}),
            'pincode': forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'ph_no' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'personal_description' : forms.Textarea(attrs= {'class': 'editable medium-editor-textarea postcontent'}), # here postcontent is user created css class
        }

class ProblemProviderForm(forms.ModelForm):
    
    class Meta:
        model = ProblemProvider
        fields = ("provider_name","provider_brief","govt_liscence_id","address","pin_code","ph_no","personal_description")
        
        widgets = {
            'provider_name' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'govt_liscence_id' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'address': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea address-field'}),
            'pincode': forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'ph_no' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'provider_brief' : forms.Textarea(attrs= {'class': 'editable medium-editor-textarea'}),
            'personal_description' : forms.Textarea(attrs= {'class': 'editable medium-editor-textarea postcontent'}), # here postcontent is user created css class
        }
