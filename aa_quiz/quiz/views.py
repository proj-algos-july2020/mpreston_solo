from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def welcome(request):
    return render(request, 'quiz/index.html')