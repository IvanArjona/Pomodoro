import json
from django.http import HttpResponse, JsonResponse
from web.models import Timer


def timers(request):
    if request.method == 'GET':
        timers = list(Timer.objects.values())
        return JsonResponse(timers, safe=False)
    elif request.method == 'POST':
        params = json.loads(str(request.body, encoding='utf-8'))
        task = Timer(**params)
        task.save()
        return HttpResponse('')