from typing import List
from django import forms
from .models import List, Item

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list_title']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item', 'description']