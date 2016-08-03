# -*- coding:utf-8 -*-

from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

class RegistrationForm(UserCreationForm): 
    role = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'role', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, error_messages={'required': 'Укажите логин'})
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), error_messages={'required': 'Укажите пароль'})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Логин или пароль не верный.")
        return self.cleaned_data

class AddingPosition(forms.Form):
    name = forms.CharField(label='Должность', max_length=150, error_messages={'required': 'Укажите должность'})
    employer = forms.CharField(label='Компания', max_length=100, error_messages={'required': 'Укажите компанию'})
    salary = forms.IntegerField(label='Зарплата', error_messages={'required': 'Укажите размер заработной платы'})
    text = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols':50,'rows':20}), error_messages={'required': 'Укажите описание вакансии'})
    image = forms.ImageField(label='Изображение', required=False)
    phone = forms.CharField(label='Контактный телефон', widget=forms.TextInput(attrs={'placeholder': '+7 (123) 456-7890'}), error_messages={'required': 'Укажите контактный телефон'})

class SearchForm(forms.Form):
    text = forms.CharField(label='Поиск вакансии', max_length=200, required=False)

