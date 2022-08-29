from django.db import models

# Create your models here.

class AutorKsiazki(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nazwisko}, {self.imie}'





    

class Ksiazki(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.ForeignKey(AutorKsiazki,on_delete=models.SET_NULL, null=True,related_name='autor')
    opis = models.TextField(blank=True,null=True)
    isbn =  models.CharField('ISBN', max_length=13, unique=True)

    
    KATEGORIA = (
        ('fsci','fantasy,science-fiction'),
        ('h','horror'),
        ('k','kryminał'),
        ('lm','literatura młodzieżowa'),
        ('lo','literatura obyczajowa'),
        ('ph','powieść historyczna'),
        ('pp','powieść przygodowa'),
        ('pn','literatura popularno-naukowa'),
        ('b','bajki'),
        ('bl','baśnie,legendy'),
        ('ld','literatura dziecięca'),
        ('o','opowiadania'),
        ('w','wiersze'),
        ('d','dramat')
    )
    kategoria = models.CharField(choices=KATEGORIA,blank=True,null=True,help_text='Kategoria',default='pp',max_length=4)

    class Meta:
        ordering = ['tytul']

    def __str__(self):
        return self.tytul




