from django import forms 
from .models import Galerie , Kontakt



class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    telephone = forms.CharField(label="Telefonnumer")
    email = forms.EmailField(label="E-Mail-address")
    class Meta:
        model = Kontakt
        fields = '__all__'


class AddPicture(forms.ModelForm):
    class Meta:
        model  = Galerie
        fields = ['name' , 'image']