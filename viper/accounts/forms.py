from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'password1',
        )
    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'First Name', 'id':'FirstName'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Last Name', 'id':'LastName'})
        self.fields['email'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Email', 'id':'Email'})
        self.fields['password'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Password', 'id':'Password'})
        self.fields['password1'].widget.attrs.update({'class':'form-control form-control-user','placeholder':'Password', 'id':'Password1'})
