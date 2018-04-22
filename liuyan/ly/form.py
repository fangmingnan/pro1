# -*- coding: utf-8 -*-
from django import forms
class liuyan(forms.Form):
    name = forms.CharField(max_length=20,min_length=3)
    email = forms.CharField(max_length=30)
    address = forms.CharField(max_length=100)
    message = forms.CharField(max_length=300)