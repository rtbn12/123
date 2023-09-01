from django import forms
from django.core.exceptions import ValidationError
from.models import Advertisment


class AdvertisementForm(forms.ModelForm):
    def __int__(self,*args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['title'].widget.attrs['class']= 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisment
        fields = ['title','description','image','price','auction']

    def clean_title(self):
        title= self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('not ?')

        return title















