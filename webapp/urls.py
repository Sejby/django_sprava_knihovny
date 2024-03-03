from django.urls import path
from . import views

urlpatterns = [
    path('', views.uvod, name="uvod"),
    path('registrace', views.registrace, name="registrace"),
    path('prihlaseni', views.prihlaseni, name="prihlaseni"),
    path('odhlaseni', views.odhlaseni, name="odhlaseni"),
    path('dashboard', views.dashboard, name="dashboard"),

]
