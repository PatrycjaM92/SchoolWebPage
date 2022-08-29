from re import template
from django.urls import path,include
from django.views.generic import TemplateView
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"ankieta",views.OdpowiedzApi)
router.register(r"pytanie",views.PytanieApi)


from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('',views.homepage,name='home'),
    path('ankieta',views.answerView,name='answer'),
    path('wpis/<int:pk>/',views.wpisDetal,name='wpis'),
    path('grono',TemplateView.as_view(template_name="blog/grono.html"),name="grono"),
    path('samorzad',TemplateView.as_view(template_name="blog/samorzad.html"),name="samorzad"),
    path('rada',TemplateView.as_view(template_name="blog/rada.html"),name="rada"),
    path('kontakt',TemplateView.as_view(template_name="blog/kontakt.html"),name="kontakt"),
    path('historia',TemplateView.as_view(template_name="blog/historia.html"),name="historia"),
    path('galeria',views.galeria,name = 'zdjecia'),
    path('dokumenty',views.dokumenty,name = 'dokumenty'),
    path('wyniki',views.wynikAnkiety,name = "wyniki"),
  
    
    path('api/',include(router.urls)),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)