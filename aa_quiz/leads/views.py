from django.shortcuts import render, HttpResponse, redirect
from .models import Lead

# Create your views here.

def index(request):
    context = {
        'all_leads': Lead.objects.all()
    }
    return render(request, 'leads/index.html', context)


def lead_detail(request):
    return render(request, 'leads/lead_detail.html')