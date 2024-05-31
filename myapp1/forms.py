from django import forms
from .models import wap,van

class mywap(forms.ModelForm):
      class Meta:
            model=wap
            fields='__all__'



class myvan(forms.ModelForm):
      class Meta:
            model=van
            fields='__all__'