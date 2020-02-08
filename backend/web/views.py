from django.http import HttpResponse, JsonResponse
from web.models import Timer


def timers(request):
    if request.method == 'GET':
        timers = list(Timer.objects.values())
        return JsonResponse(timers, safe=False)