from django import forms
from appTwo import models

class myform(forms.ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
