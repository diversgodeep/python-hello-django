from django import forms
from hello.models import logMessage

class logMessageForm(forms.ModelForm):
  class Meta:
    model = logMessage
    fields = ("message",)  