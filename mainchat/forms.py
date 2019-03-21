from django import forms
from .models import Message


class ContentForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('message_text',)
