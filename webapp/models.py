from django.db import models

class Kniha(models.Model):
    nazev_knihy = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    zanr = models.CharField(max_length=50)
    pocet_stran = models.IntegerField()
    datum_vytvoreni = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Název knihy: {self.nazev_knihy} Od autora: {self.autor}"