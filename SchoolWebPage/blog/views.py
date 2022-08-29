from multiprocessing import context
from re import A
from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404,HttpResponseRedirect
from .models import Wpis,Ankieta,Uzytkownicy,Odpowiedz,Zdjecia,Dokumenty
from .forms import OdpowiedzForm,DodajPytanieForm
from rest_framework import viewsets
from .serializer import  OdpowiedzSerializer, PytanieSerializer
import pandas as pd
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as mtick
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import urllib,base64


# Create your views here.

def homepage(request):
    wpis = Wpis.objects.all()
    return render(request,'blog/wpis.html',{"wpis":wpis})


def wpisDetal(request,pk):

    wpis= get_list_or_404(Wpis,pk=pk)
  
    return render(request,'blog/detalwpis.html',{'wpis' : wpis})



def addQuestion(request):    
    context = {}
    form=DodajPytanieForm()
    if(request.method=='POST'):
        form=DodajPytanieForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'blog/addQuestion.html',context)


def answerView(request):
    
    questions =Ankieta.objects.all()
    odpowiedzi = Odpowiedz.objects.all()
    
    if (request.method=='POST'):
        
        for q in questions: 
            
            form = OdpowiedzForm(request.POST)
            ans=request.POST.get(q.pytanie)
            pyt = Ankieta.objects.get(id=q.id)
            odpowiedz =Odpowiedz.objects.create(pyt=pyt,odpowiedz=ans)
            odpowiedz.save()
                        
        return HttpResponseRedirect('wyniki')
        #return render(request,'blog/ankieta.html',{'form':form,'questions':questions,'odpowiedzi':odpowiedzi} )      
                    
    else:
        form=OdpowiedzForm()

    return render(request,'blog/ankieta.html',{'form':form,'questions':questions,'odpowiedzi':odpowiedzi} )   


def wynikAnkiety(request):
    ankieta = Ankieta.objects.all().values()
    odpowiedz = Odpowiedz.objects.all().values()
    df1 = pd.DataFrame(ankieta)
    df2 = pd.DataFrame(odpowiedz)
    df3 = pd.merge(df2,df1,left_on='pyt_id',right_on='id')
    print(df1)
    df3 = df3[['odpowiedz','pytanie','pyt_id','numer_pytania']]
    df3 = df3.groupby(['pytanie',"odpowiedz",'pyt_id']).odpowiedz.agg('count').to_frame("count").reset_index()
    json_records = df3.reset_index().to_json(orient = 'records')
    arr =[]
    arr = json.loads(json_records)
   
    def graph():
        
        se = set(df3['pytanie'])
        imglist = []
        
        ile = df3.loc[df3['pyt_id']==1]
        ile = ile['count'].to_numpy()
        ile =sum(ile)

        for i,val in enumerate(se,1):
       
            fig = plt.figure(figsize=(6,4))
            ax = fig.subplots()
            print(i)
            
        
            #xx= df3.loc[df3['pyt_id']==i]
            xx= df3.loc[df3['pytanie']==val]
           
            #yy= df3.loc[df3['pyt_id']==i]
            yy= df3.loc[df3['pytanie']==val]
        
            

            x = xx['odpowiedz'].to_numpy()
            y= yy['count'].to_numpy()
            
            y = [round(i/ile*100,2) for i in y]
  
            ax.margins(0.5)

            ax.set_title(val,loc='left')
            print('pytanir ',val)
            
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        
            p1 = ax.bar(x,y,width =0.3,color=['black', 'red', 'blue', 'cyan'])
            ax.yaxis.set_major_formatter(mtick.PercentFormatter())
        
            for rect1 in p1:
                height = rect1.get_height()
                plt.annotate( "{}%".format(height),(rect1.get_x() + rect1.get_width()/2, height+.03),ha="center",va="bottom",fontsize=12)
            
            ax.tick_params(axis='x', labelrotation = 90)
            
            buf = io.BytesIO()
            fig.savefig(buf,format='png',bbox_inches = "tight")
            buf.seek(0)
            string = base64.b64encode(buf.read())
            uri = urllib.parse.quote(string)

            
            imglist.append(uri)


        return imglist
    wykr = graph()

    context = {'df':arr,
               'graph':wykr}

    #print(df3)

    return render (request,'blog/wyniki.html',context)
    


def galeria(request):
    zdjecia = Zdjecia.objects.all()
    return render(request,'blog/galeria.html',{'zdjecia':zdjecia})

def dokumenty(request):
    dokumenty = Dokumenty.objects.all()
    return render(request,'blog/dokumenty.html',{'dokumenty':dokumenty})



class OdpowiedzApi(viewsets.ModelViewSet):
    queryset=Odpowiedz.objects.all()
    serializer_class = OdpowiedzSerializer

class PytanieApi(viewsets.ModelViewSet):
    queryset = Ankieta.objects.all()
    serializer_class= PytanieSerializer

