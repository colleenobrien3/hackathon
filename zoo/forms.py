from django import forms
from .models import ZooUser

class ZooUserForm(forms.ModelForm):

    class Meta:
        model = ZooUser
        fields = ('name', 'email', 'newsletter' 'image_url')

