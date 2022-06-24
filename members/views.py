from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from . forms import EditProfileForm, PasswordChangingForm, UsersRegisterForm

class PasswordsChangeView(PasswordChangeView):
    form_class= PasswordChangingForm
    success_url=reverse_lazy('login')
    

class UserRegisterView(generic.CreateView):
    form_class= UsersRegisterForm
    template_name= 'registration/register.html'
    success_url= reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name= 'registration/edit_profile.html'
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user

