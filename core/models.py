from django.db import models

# Create your models here.
class Galerie(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name



class Kontakt(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=130)
    telephone = models.CharField(max_length=100)
    Ihre_Nachricht = models.TextField(max_length=400)
    sent_data_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name