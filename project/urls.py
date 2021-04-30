from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))  #viittaa app kansion urls.py 
]
# eli jos mennään juureen käyttää sovellus app kansion urls.py tiedoston urleja
# jos taas laitetaan sovelluksen localhost:8000/admin niin sitten ylemmän määrityksen mukaan