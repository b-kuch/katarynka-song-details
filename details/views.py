# Create your views here.
from django.http import HttpResponse, JsonResponse

from .models import Song


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def trending_songs(request):
    return JsonResponse(
        {"songs": list(map(Song.toDict, Song.objects.all()))}
    )
