from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email')


class PasswordChangingForm(PasswordChangeForm):
    old_password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model= User
        fields = ('old_password','new_password1','new_password2')

class UsersRegisterForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    password2= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model= User
        fields = ('username','password1','password2')