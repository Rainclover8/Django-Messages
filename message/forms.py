from django import forms
from .models import *

class MessageForm(forms.ModelForm):
    class Meta:
        model = createMessage
        fields = ['username','description']