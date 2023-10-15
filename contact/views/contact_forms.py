from django import forms
from django.shortcuts import render

from contact.models import Contact


class ContactForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email'
        )


def create(request):
    if request.methos == 'POST':
        context = {
            'form': ContactForms(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )
