from django import forms
from django.template.defaultfilters import default
from pycparser.c_ast import Default

from website.models import Contact,Newsletter


class NameForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ConatactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'