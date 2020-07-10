from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def welcome(request):
    return HttpResponse("Take the Art Advisory Quiz")