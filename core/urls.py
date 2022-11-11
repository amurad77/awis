from cgitb import handler
from django.urls import path, include
from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('', views.index),
    path('about/', views.about),
    path('opportunities/', views.opportunities),
]