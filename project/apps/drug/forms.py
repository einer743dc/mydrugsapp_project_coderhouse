from django import forms
from .models import Drug

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'company', 'composition', 'package_qty', 'drugtype', 'restricted', 'stock', 'price','drug_picture']