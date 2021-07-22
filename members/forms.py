from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields =('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args , **kwargs) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class ProfileForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=User
        fields =('username','first_name','last_name','email')

class PasswordChangedForm(PasswordChangeForm):
    old_password= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model=User
        fields =('username','first_name','last_name','email','password1','password2')
