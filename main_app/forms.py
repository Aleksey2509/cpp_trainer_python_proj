from django import forms
from .models import CppExample


class CppExampleForm(forms.ModelForm):
    class Meta:
        model = CppExample
        fields = ["code", "status", "explanation"]
        widgets = {
            "code": forms.Textarea(
                attrs={
                    "rows": 6,
                    "style": "width: 100%; padding: 8px",
                }
            ),
            "status": forms.TextInput(
                attrs={
                    "placeholder": "e.g. undefined behavior",
                    "style": "width: 100%; padding: 8px",
                }
            ),
            "explanation": forms.Textarea(
                attrs={
                    "rows": 4,
                    "style": "width: 100%; padding: 8px",
                }
            ),
        }
