from .models import post
from django import forms
class frm(forms.ModelForm):
    class Meta:
        model=post
        fields=['post','date']