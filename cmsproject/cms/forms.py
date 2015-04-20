# -*- coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'contents')