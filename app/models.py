from django.db import models

class ElainKategoria(models.Model):
    ryhma = models.CharField(max_length=24)
    objects = models.Manager() # pylint luuleman virheilmoituksen poistamiseen - ei välttämätön
    

class Elain(models.Model):
    pvm = models.DateTimeField(auto_now_add=True,null=True)
    nimi = models.CharField(max_length=50,default='testi')
    ryhma = models.ForeignKey(ElainKategoria,on_delete=models.CASCADE,default=None)
    huomioon = models.TextField()
    objects = models.Manager() # pylint luuleman virheilmoituksen poistamiseen - ei välttämätön