import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Song


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def trending_songs(request):
    return HttpResponse(json.dumps(list(map(Song.toDict, Song.objects.all()))),
                        content_type="application/json")
