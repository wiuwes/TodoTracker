from django.forms import ModelForm, TextInput,Textarea,DateInput
from django import forms
from datetime import datetime
from django.utils import timezone
from .models import Notes , Commentary

INT_PROCESS = [
    ('0', 'open'),
    ('1', 'in process'),
    ('2', 'verefication needed'),
    ('3', 'close'),
]

class Form_for_Notes(ModelForm):
    status = forms.ChoiceField(choices=INT_PROCESS)
    form = forms.CharField(max_length=100)
    class Meta:
        model = Notes
        fields = ['text','title']
        widgets = {
        "title": TextInput(attrs={'class': '','placeholder': 'Title'}),
        "text": Textarea(attrs={'class': '','placeholder': 'Input text','rows': 10}),
        }

class Edit_status(forms.Form):
    form = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=INT_PROCESS)

class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['commentary']
        widgets = {
            "commentary": Textarea(attrs={'class': '', 'placeholder': 'Input text', 'rows': 10}),
        }
