from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
   
    class Meta:     
        model =Note
        fields = ("title", "description", "due_date", "type")
        # widgets = {
        # 'title': forms.TextInput(attrs={'class': 'form-control'}),
        # }
    def __init__(self, *args, **kwargs): 
        super(NoteForm, self).__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control'})
        self.fields['due_date'].widget.attrs.update({'class' : 'form-control'})
        self.fields['type'].widget.attrs.update({'class' : 'form-control'})

       