from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from api import views

urlpatterns=[

    path('actDiarias/', views.ActDiariasList.as_view()),
    path('cliente/', views.ClienteList.as_view()),
    path('colab/', views.ColabList.as_view()),
    path('act/', views.ActList.as_view()),
    path('servicio/', views.ServicioList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
