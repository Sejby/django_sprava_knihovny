from django.db import models

class Kniha(models.Model):
    nazev_knihy = models.CharField(max_length=200, null=False)
    autor = models.CharField(max_length=200, null=False)
    zanr = models.CharField(max_length=50, null=True)
    pocet_stran = models.IntegerField(null=True)
    rok_vydani = models.IntegerField(null=False)
    datum_vytvoreni = models.DateTimeField(auto_now=True, null=True)
    obrazek = models.TextField(null=False)

