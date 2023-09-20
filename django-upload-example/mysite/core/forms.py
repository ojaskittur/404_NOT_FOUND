from django import forms
from .models import Book

class ClearableTextInput(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Set the default value to "No slot" if the value is empty
        if not value:
            value = 'No slot'
        return super().render(name, value, attrs, renderer)

class BookForm(forms.ModelForm):
    slot = forms.CharField(
        label='Slot',
        required=False,
        max_length=255,
        widget=ClearableTextInput(attrs={'onfocus': 'clearDefaultValue(this)', 'onblur': 'restoreDefaultValue(this)'}),
    )

    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf')
        labels = {
            'title': 'Subject',
            'author': 'Teacher',
        }
