from .models import Odpowiedz,Ankieta
from rest_framework import serializers

class OdpowiedzSerializer(serializers.ModelSerializer):

    class Meta:
        model=Odpowiedz
        fields =['id','pyt','odpowiedz']


class PytanieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Ankieta
        fields = ['id','pytanie']