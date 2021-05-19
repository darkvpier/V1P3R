from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError('Password is too short')

class ProfileCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'password1',
        )
        widgets = {
    'password': forms.PasswordInput(),
    'password1': forms.PasswordInput()
}
    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.required = True
        self.fields['first_name'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'First Name', 'id':'FirstName'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Last Name', 'id':'LastName'})
        self.fields['email'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Email', 'id':'Email'})
        self.fields['password'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Password', 'id':'Password'})
        self.fields['password1'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Password', 'id':'Password1'})

    def clean(self):
        super(ProfileCreationForm, self).clean()
        email = self.cleaned_data['email']
        if User.objects.get(email=email):
            self.add_error('email', 'Email already exists')
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            self.add_error('password1' ,'Password much match')
    
    def save(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        return User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)


    