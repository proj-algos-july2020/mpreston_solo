from django.urls import path
from . import views

urlpatterns = [
   path('', views.q_welcome),
   path('intent', views.q_intent),
   path('intent/process', views.process_intent),
   path('info_request', views.q_info_request),
   path('info_request/process', views.process_info_request),
   path('contact', views.q_contact),
   path('contact/process', views.process_contact),
]