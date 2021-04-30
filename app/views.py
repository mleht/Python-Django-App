from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import ElainKategoria, Elain

def home(request):
    return render (request, "home.html")

#login & logout
def kirjaudu(request):
    kayttaja = request.POST['ktunnus']
    salasana = request.POST['salasana']
    kayttaja = authenticate(username = kayttaja, password = salasana)
    if kayttaja:
        login(request, kayttaja)
        mydictionary = {'kayttaja' : kayttaja}
        return render(request, 'home.html', context=mydictionary)
    else:
        return render(request, 'kirjautumisvirhe.html')
	
def kirjaudu_ulos(request):
    logout(request)
    return render(request, 'home.html')
	
# eläinkategoriat
def elainkategoriat(request):
    if not request.user.is_authenticated:
        return render(request, 'kirjautumisvaatimus.html')
    else:
        elainkategoriatlista = ElainKategoria.objects.all() # haetaan kaikki 
        mydictionary = {'kategoriat': elainkategoriatlista} 
        return render (request, "kategoriat.html", context=mydictionary)

def lisaaelainkategoria(request):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            ryhma = request.POST['kategoria']
            ElainKategoria(ryhma = ryhma).save()
            return redirect(request.META['HTTP_REFERER'])
    except:
        return render(request, 'virhe.html')

def muokkaa_elainkategoria_get(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            kategoria = ElainKategoria.objects.filter(id = id)
            mydictionary = {'kategoria': kategoria}
            return render (request,"kategoria_muokkaa.html",context=mydictionary)
    except:
        return render(request, 'virhe.html')
    
def muokkaa_elainkategoria_post(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            kategoria = ElainKategoria.objects.get(id = id)
            kategoria.ryhma = request.POST['kategoria']
            kategoria.save()
            return redirect(elainkategoriat)
    except:
        return render(request, 'virhe.html')

def poista_elainkategoria_get(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            kategoria = ElainKategoria.objects.filter(id = id)
            mydictionary = {'kategoria': kategoria}
            return render (request,"kategoria_poista.html",context=mydictionary)
    except:
        return render(request, 'virhe.html')

def poista_elainkategoria_post(request,id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            ElainKategoria.objects.filter(id = id).delete() 
            return redirect(elainkategoriat)
    except:
        return render(request, 'virhe.html')

#Eläimet

def elaimet(request):
    if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
    else:
        elaimet = Elain.objects.all()
        kategoriat = ElainKategoria.objects.all()
        myDictionary= {
            'elaimet' : elaimet,
            'kategoriat' : kategoriat,
        }
        return render (request, "elaimet.html", context=myDictionary)

def lisaaelain(request):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            kategoria = ElainKategoria.objects.get(ryhma=request.POST.get('kategoria'))
            uusi_elain = Elain(
                nimi = request.POST.get('nimi'),
                huomioon = request.POST.get('huomioon'),
                ryhma = kategoria,
            )
            uusi_elain.save()
            return redirect(request.META['HTTP_REFERER'])
    except:
        return render(request, 'virhe.html')

def muokkaa_elain_get(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            muokattava = Elain.objects.filter(id = id)
            mydictionary = {'muokattava': muokattava}
            return render (request,"elain_muokkaa.html",context=mydictionary)
    except:
        return render(request, 'virhe.html')

def muokkaa_elain_post(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            muokattu = Elain.objects.get(id = id)
            muokattu.nimi = request.POST['nimi']
            muokattu.huomioon = request.POST['huomioon']
            muokattu.save()
            return redirect(elaimet)
    except:
        return render(request, 'virhe.html')

def poista_elain_get(request, id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            poistettava = Elain.objects.filter(id = id)
            mydictionary = {'poistettava': poistettava}
            return render (request,"elain_poista.html",context=mydictionary)
    except:
        return render(request, 'virhe.html')

def poista_elain_post(request,id):
    try:
        if not request.user.is_authenticated:
            return render(request, 'kirjautumisvaatimus.html')
        else:
            Elain.objects.filter(id = id).delete() 
            return redirect(elaimet)
    except:
        return render(request, 'virhe.html')

