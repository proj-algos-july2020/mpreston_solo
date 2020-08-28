from django.urls import path
from . import views

urlpatterns = [
   path('', views.about),
   path('start', views.q_welcome),
   path('intent', views.q_intent),
   path('intent/process', views.process_intent),
   path('info_request', views.q_info_request),
   path('info_request/process', views.process_info_request),
   path('spec_space', views.q_spec_space),
   path('spec_space/process', views.process_spec_space),
   path('persona', views.q_persona),
   path('persona/process', views.process_persona),
   path('category', views.q_category),
   path('category/process', views.process_category),
   path('subject', views.q_subject),
   path('subject/process', views.process_subject),
   path('style', views.q_style),
   path('style/process', views.process_style),
   path('size', views.q_size),
   path('size/process', views.process_size),
   path('contact', views.q_contact),
   path('contact/process', views.process_contact),
   path('result/<int:id>', views.q_result),
]