from django import forms

class LoginForm(forms.Form):
    
    username = forms.CharField(label="Correo electrónico",required=True, max_length=25, widget=forms.TextInput(attrs={ 'type':"text", 'placeholder':" cliente@hotmail.com", 'class': "default-input"}))
    
    password = forms.CharField(label="Contraseña",required=True, max_length=25, widget=forms.TextInput(attrs={ 'type':"password", 'placeholder':"  Contraseña", 'class': "default-input"}))
      
class NewUserForm(forms.Form):
        
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={ 'type':"text", 'placeholder':" cliente@hotmail.com", 'class': "default-input"}))

	username = forms.CharField(label="Usuario",required=True, max_length=25, widget=forms.TextInput(attrs={ 'type':"text", 'placeholder':" John Doe", 'class': "default-input"}))

	password1 = forms.CharField(label="Contraseña",required=True, max_length=25, widget=forms.TextInput(attrs={ 'type':"password", 'placeholder':"  Contraseña", 'class': "default-input"}))

	password2 = forms.CharField(label="Repita su contraseña",required=True, max_length=25, widget=forms.TextInput(attrs={ 'type':"password", 'placeholder':"  Contraseña", 'class': "default-input"}))