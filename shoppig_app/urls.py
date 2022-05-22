from django.urls import path
from .views import Products1,Mycart1
from . import views

urlpatterns=[
    path('',Products1.as_view()),
    path('Mycart1',Mycart1.as_view()),
    path('formm',views.formm,name='formm'),
    path('savedborders',views.savedborders,name='savedb'),
]

