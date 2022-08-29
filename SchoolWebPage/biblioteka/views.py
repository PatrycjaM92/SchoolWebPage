from django.shortcuts import render
from biblioteka.models import Ksiazki,AutorKsiazki
from django.db.models import Q 
# Create your views here.


def ksiazki(request):
    ksiazki = Ksiazki.objects.all()
    print(ksiazki)
    szukana = request.GET.get('search')
    if szukana:   
        ksiazki = Ksiazki.objects.filter(Q(tytul__icontains=szukana) )
        print(ksiazki)
        return render(request,'blog/znalezione.html',{'ksiazki':ksiazki})
        
    else:   
        ksiazki = Ksiazki.objects.all().order_by("-tytul")
        print('nie ma')
    
    context = {
        'ksiazki':ksiazki,
            }

    return render(request,'blog/biblioteka.html',context)