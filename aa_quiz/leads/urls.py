from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('detail/', views.lead_detail),
]