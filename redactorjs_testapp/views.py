# -*- coding: utf-8 -*-

__author__ = 'ufian'

from django.shortcuts import render_to_response
from django import forms

from redactorjs.widgets import RedactorjsTextarea

class RedactorForm(forms.Form):
    text = forms.CharField(
        label='Example field',
        widget=RedactorjsTextarea(
            attrs={'id': 'content'},
            redactor_options={}
        )
    )

# Example view with form
def index(request):
    form = RedactorForm()
    return render_to_response('index.html', {'form': form})
