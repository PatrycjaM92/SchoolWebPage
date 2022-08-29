from django.contrib import admin
from .models import Wpis,Ankieta,Uzytkownicy,Odpowiedz,Zdjecia,Dokumenty
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


admin.site.register(Ankieta)
admin.site.register(Uzytkownicy)
admin.site.register(Odpowiedz)
admin.site.register(Zdjecia)
admin.site.register(Dokumenty)

admin.site.register(Wpis)

class WpisAdmin(admin.ModelAdmin):
    model=Wpis
    list_display = ('tytul','opis','data_utworzenia','data_publikacji','czyOpublikowane','autor')
    list_filter = ('czyOpublikowane','data_publikacji')
    search_fields = ('tytul','autor','opis')

# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('opis','tresc')


