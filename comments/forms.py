from django import forms

from .models import Comment


class CommentForm(forms.ModelForms):
    class Meta:
        model = Comment
        fields = ["comment"]
