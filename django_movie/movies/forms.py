from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Формы отзыва"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
