from dataclasses import fields
from pyexpat import model
from django import forms
from .models import asanaModel
from django.forms import ModelForm
class asanaForm(ModelForm):
     class Meta:
        model = asanaModel
        fields = ["taskname","notes"]
        exclude = ('task_id',)
