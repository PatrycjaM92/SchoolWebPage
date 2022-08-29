
from django.urls import path
from django.views.generic import TemplateView
from .import views

from django.conf import settings

urlpatterns = [
    #path('historia',TemplateView.as_view(template_name="blog/biblioteka.html"),name="biblioteka"),
    path('biblioteka',views.ksiazki,name="biblioteka"),

]

