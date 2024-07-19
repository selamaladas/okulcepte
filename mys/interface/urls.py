from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dersler/', views.dersler, name='dersler'), 
    path('galeri/', views.galeri, name='galeri'), 
    path('hocalar/', views.hocalar, name='hocalar'), 
    path('iletisim/', views.iletisim, name='iletisim'), 
    path('index/', views.index, name='index'), 
    path('uyeolmak/', views.uyeolmak, name='uyeolmak'), 
    


]