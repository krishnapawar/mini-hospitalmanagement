from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import userprofile
from.models import*



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProUpdate(forms.ModelForm):
	pimg = forms.ImageField()

	class Meta:
		model = userprofile
		fields = ['pimg']





class Createnewac(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class pupdate(forms.ModelForm):
	class Meta:
		model = admitpasent
		fields =['name','gender','birthdate','address','diseases','admit_charge','user']