from django import forms
from .models import Account



class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}))
    
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password',]
    
    def __init___(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            