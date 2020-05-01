from django import forms
from .models import BookEntry

class DateInput(forms.DateInput):
    input_type = 'date'

class bookForm(forms.ModelForm):

    class Meta:
        model = BookEntry
        fields = ('title', 'author', 'Published', 'PagesNum', 'BookType')
        labels = {
            'PagesNum': 'Number of Pages',
            'BookType': 'Category', 
        }
        widgets = {'Published':DateInput()}

    def __init__(self,*args, **kwargs):
        super(bookForm, self).__init__(*args,**kwargs)
        self.fields['Published'].required = False
        self.fields['PagesNum'].required = False
        self.fields['BookType'].required = False
