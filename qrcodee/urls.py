from django.urls import path
from . import views 

urlpatterns = [
    
    path('' , views.index, name='index'),
    path('json/<int:rib>/<str:DD>/<str:DF>' , views.getJson, name='json'),
    path('clientqr/<str:file>' , views.getJsonClient, name='jsonclient'),
    path('clientqrdec/C:/fakepath/<str:filename>' , views.getClientDecode, name='jsonclientdecode'),
    path('clientqrdec2/C:/fakepath/<str:filename>' , views.getClientDecode2, name='jsonclientdecode2'),
    path('selectRIB' , views.ListeRib, name='ListeRib'),
    path('decode' , views.getDecode, name='decode'),
    path('rib' , views.Rib, name='rib'),
    path('compte/<int:rib>' , views.GetCompte, name='compte'),
    path('rib/<int:rib>' , views.GetInfo, name='infos')
]