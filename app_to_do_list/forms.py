from django import forms
from .models import List, Item, Subitem

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['list_title']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item', 'description']

class SubitemForm(forms.ModelForm):
    class Meta:
        model = Subitem
        fields = ['item', 'description']