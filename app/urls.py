from django.urls import path
from . import views #eli importoidaan saman kansion views.py tiedostosta

urlpatterns = [
    path('', views.home, name ='home'),

    #login
    path('kirjaudu/', views.kirjaudu, name='kirjaudu'),
    path('ulos/', views.kirjaudu_ulos, name='kirjaudu_ulos'),

    #eläinkategoriat
    path('elainkategoriat/', views.elainkategoriat, name='kategoriat'),
    path('lisaa-kategoria/', views.lisaaelainkategoria, name='lisaa-kategoria'),
    path('muokkaa-kategoria-get/<int:id>/', views.muokkaa_elainkategoria_get, name='muokkaa-kategoria-get'),
    path('muokkaa-kategoria-post/<int:id>/', views.muokkaa_elainkategoria_post, name='muokkaa-kategoria-post'),
    path('poista-kategoria-get/<int:id>/', views.poista_elainkategoria_get, name='poista-kategoria-get'),
    path('poista-kategoria-post/<int:id>/', views.poista_elainkategoria_post, name='poista-kategoria-post'),

    #eläimet
    path('elaimet/', views.elaimet,name='elaimet'),
    path('lisaa-elain/', views.lisaaelain, name='lisaa-elain'),
    path('muokkaa-elain-get/<int:id>/', views.muokkaa_elain_get, name='muokkaa-elain-get'),
    path('muokkaa-elain-post/<int:id>/', views.muokkaa_elain_post, name='muokkaa-elain-post'),
    path('poista-elain-get/<int:id>/', views.poista_elain_get, name='poista-elain-get'),
    path('poista-elain-post/<int:id>/', views.poista_elain_post, name='poista-elain-post'),
]

