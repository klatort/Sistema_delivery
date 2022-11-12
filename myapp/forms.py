from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="",required=False, max_length=25, widget=forms.TextInput(attrs={ 'type':"text", 'placeholder':"  Usuario", 'class': "default-input"}))
    password = forms.CharField(label="",required=False, max_length=25, widget=forms.TextInput(attrs={ 'type':"password", 'placeholder':"  Contraseña", 'class': "default-input"}))