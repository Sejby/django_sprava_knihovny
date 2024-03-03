from django.urls import path
from . import views

urlpatterns = [
    path('', views.uvod, name="uvod"),
    path('registrace', views.registrace, name="registrace"),
    path('prihlaseni', views.prihlaseni, name="prihlaseni"),
    path('odhlaseni', views.odhlaseni, name="odhlaseni"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('pridat_knihu', views.pridat_knihu, name="pridat_knihu"),
    path('smazat_knihu/<int:pk>', views.smazat_knihu, name="smazat_knihu"),
    path('upravit_knihu/<int:pk>', views.upravit_knihu, name="upravit_knihu")
]
