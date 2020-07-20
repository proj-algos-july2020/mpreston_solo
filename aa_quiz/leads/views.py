from django.shortcuts import render, HttpResponse, redirect
from .models import Lead
import json

# Create your views here.


def index(request):
    context = {
        'all_leads': Lead.objects.all(),
    }
    return render(request, 'leads/index.html', context)


def lead_detail(request, id):

    this_lead = Lead.objects.get(id=id)
    this_brief = this_lead.quiz_brief

    brief_dict = json.loads(this_brief)

    context = {
        'lead': Lead.objects.get(id=id),
        'brief': brief_dict,
    }
    return render(request, 'leads/lead_detail.html', context)