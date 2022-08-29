from dataclasses import fields
from django import forms
from .models import  Ankieta, Odpowiedz
from django.forms import ModelForm

# class AnswerForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = ('answer',)
class OdpowiedzForm(forms.ModelForm):
    #answer=forms.CharField(label='Odpowedź ',max_length=250)


    class Meta:
        model= Odpowiedz
        fields = ('odpowiedz',)
   
class DodajPytanieForm(ModelForm):
    class Meta:
        model = Ankieta
        fields = ('pytanie','opcja1','opcja2','opcja3','opcja4')
        