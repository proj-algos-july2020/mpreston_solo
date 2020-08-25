from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>', views.lead_detail),
]