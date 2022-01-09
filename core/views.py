from django.shortcuts import render , redirect
from .models import Galerie , Kontakt
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request , 'core/index.html' , {})


def aboutme(request):
    return render(request , 'core/über-mich.html' , {})


def impressum(request):
    return render(request , 'core/impressum.html',{})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request , "Ihre Nachricht wurde gesendet")
            return redirect(reverse('main:contact_page'))
        else:
            messages.warning(request , "Ihre Nachricht wurde nicht gesendet")
            return redirect(reverse('main:contact'))
    else:
        form = ContactForm()
        
    return render(request , 'core/kontakt.html', {
        'form':form
    })

def galerie(request):
    galerie = Galerie.objects.all()
    return render(request , 'core/galerie.html',{
        'galerie':galerie
    })