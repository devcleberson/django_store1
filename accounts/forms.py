from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Digite a senha',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirme a senha',
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Digite o primeiro nome'  
        self.fields['last_name'].widget.attrs['placeholder'] = 'Digite o sobrenome' 
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Digite o número de telefone' 
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o endereço de e-mail' 
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'    