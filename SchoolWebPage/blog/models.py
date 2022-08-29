from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from django.conf import settings

# Create your models here.

class Uzytkownicy(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.user.get_username()

class Wpis(models.Model):
    class Meta:
        ordering = ['data_publikacji']
    tytul = models.CharField(max_length=250,unique=True)
    opis = models.CharField(max_length=350,blank=True,null=True)
    tresc = models.TextField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    data_modyfikacji = models.DateTimeField(auto_now=True)
    data_publikacji = models.DateTimeField(blank=True,null=True)
    czyOpublikowane = models.BooleanField(default=False)
    autor = models.ForeignKey(Uzytkownicy,on_delete=models.CASCADE)
    zdjecie = models.ImageField(blank=True,null=True)
    
    def __str__(self):
        return self.tytul

class Zdjecia(models.Model):
    tytul = models.ForeignKey(Wpis,related_name='wpis',on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'galeria/')

    


class Dokumenty(models.Model):
    nazwa = models.CharField(max_length=200)
    plik = models.FileField(upload_to="dokumenty")

    def __str__(self):
        return self.nazwa

class Ankieta(models.Model):
    pytanie = models.CharField(max_length=200)
    opcja1=models.CharField(max_length=100,blank=True,null=True)
    opcja2=models.CharField(max_length=100,blank=True,null=True)
    opcja3=models.CharField(max_length=100,blank=True,null=True)
    opcja4=models.CharField(max_length=100,blank=True,null=True)
    numer_pytania = models.IntegerField(default=1)

    def __str__(self):
        
        return self.pytanie

class Odpowiedz(models.Model):
    pyt = models.ForeignKey(Ankieta,on_delete=models.CASCADE)
    odpowiedz = models.CharField(max_length=250)

    def __str__(self):
        return self.odpowiedz


