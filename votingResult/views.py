from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def votingResult(request):
    return HttpResponse("This is my Voting Result Page")
