from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<slug:slug>/', views.article_detail),
]
