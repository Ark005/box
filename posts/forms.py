from .models import Box,Box1,Document
from django import forms
import datetime


class BoxForm(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        super(BoxForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control1',
            })

    class Meta:
        model = Box
        fields = ("__all__")
        

class Box1Form(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        super(Box1Form, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form1-control',
            })

    class Meta:
        model = Box1
        fields = ("__all__")
    

     

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


