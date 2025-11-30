from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'content': forms.Textarea(attrs={'class': 'form-control my-3'})
        }
        labels = {
            'content' : 'What is on your mind today?'
        }
        
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise forms.ValidationError("Title must have the word 'Django'")
    #     return title
        