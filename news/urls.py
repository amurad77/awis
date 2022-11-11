from cgitb import handler
from django.urls import path, include
from . import views

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('news/', views.news),
    path('news-detail/<slug:slug>/', views. news_details, name='news_details'),
]