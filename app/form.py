from django.forms import ModelForm, fields
from django import forms
# from django .contrib.auth.models import User
from .models import registartion
from .models import login
from .models import forgot
from .models import contact
from .models import subscribe

class Reg(forms.ModelForm):
    # forms.ModelForm
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = registartion
        fields = ['email', 'username', 'password', 'confirm_password','birth_date','gender','phone_number']

class Log(forms.ModelForm):
    class Meta:
        model = login
        fields = ['email', 'username', 'password']
        
class Forgot(forms.ModelForm):
    class Meta:
        model = forgot
        fields = ['email']

class Contact(forms.ModelForm):
    class meta:
        model = contact
        fields = ['name','subject','email','message']

class Subscribe(forms.ModelForm):
    class meta:
        model = subscribe
        fields = ['email']
  

        
        
        
        