from django.urls import path
from . import views

urlpatterns=[

path('gas/',views.gas), 

path('has/',views.has)

]
