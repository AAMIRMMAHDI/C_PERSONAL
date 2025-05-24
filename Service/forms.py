from django import forms
from .models import ServiceComment

class ServiceCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment...'}),
        }


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceComment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your comment...'}),
        }