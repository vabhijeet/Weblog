from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,ProfileForm,PasswordChangedForm
from django.urls import reverse_lazy

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangedForm
    # form_class=PasswordChangeForm
    templete_name='registration/change-password.html'
    success_url=reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password-success.html',{})

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=ProfileForm
    template_name='registration/profile.html'
    success_url=reverse_lazy('home')
    def get_object(self):
        return self.request.user
# Create your views here.
