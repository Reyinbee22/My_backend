from django import forms
from .models import *

class  StudentForm(forms.ModelForm):
    name= forms.CharField(label='name', required=True)
    age = forms.IntegerField(label='Age', required=True)
    address = forms.CharField(label='Address', required=True)
    parent = forms.ModelChoiceField(queryset=Parent.objects.all(), required=False)
    phone_number = forms.CharField(label='Phone Number', required=True)  # Use CharField for phone numbers
    hobby= forms.CharField(label="hobbies", required=True)


    class Meta:
        model=Student
        fields=["name","age","address","parent","phone_number","hobby"]
        

     
class ParentForm(forms.ModelForm):
    name= forms.CharField(label='name', required=True)
    occupation= forms.CharField(label='Occupation', required=True)

    class Meta:
        model = Parent
        fields = ['name', 'occupation']