# -*- coding: UTF-8-*-
from __future__ import unicode_literals
from django import forms
from django.contrib.auth.models import User
from carreras.models import Usuario
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.core.validators import RegexValidator
from django.utils.translation import ugettext, ugettext_lazy as _


class LoginForm(forms.Form):
	username = forms.CharField(
        label=("Nombre de usuario"))
	password = forms.CharField(
        widget=forms.PasswordInput(),
        label=("Contraseña"))

#class RegistrarForm(forms.Form):
#	username = forms.CharField()
#	password = forms.CharField(widget=forms.PasswordInput())
#	email = forms.EmailField()

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=("Mínimo 8 caracteres"),
    )
    password2 = forms.CharField(
        label=_("Reescribir contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Ingrese nuevamente la contraseña para verificar"),
    )

    class Meta:
        model = User
        fields = ['username']
        #field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = "Letras, dígitos y @/./+/-/_ solamente"
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas NO son iguales")
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user