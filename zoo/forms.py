from django import forms
from .models import ZooUser

class ZooUserForm(forms.ModelForm):

    class Meta:
        model = ZooUser
        fields = ('first_name', 'last_name', 'email', 'newsletter')

