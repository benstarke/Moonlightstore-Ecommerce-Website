from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class UserUpdateForm(ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = '__all__'



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = delivery
        fields = ['hostel','phoneNumber','delivered_at']



class ContactForm(forms.ModelForm):
    class Meta:
            model = contact
            fields = [ 'name', 'email', 'subject', 'message' ]