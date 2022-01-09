from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('' , views.home , name="home"),
    path('aboutme/' ,views.aboutme , name="about" ),
    path('impressum/' , views.impressum , name="impressum"),
    path('contact/' , views.contact , name="contact"),
    path('galerie/' , views.galerie , name="galerie"),
]