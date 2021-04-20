from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.utils import json

from .utils import maze_utils
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def maze_view(request):
    try:
        N = request.data.get('N')
        grid = request.data.get('grid')
        res = maze_utils.mario_save_princess(N, grid)
        return HttpResponse(json.dumps(res))
    except:
        return HttpResponse('Unknown request data', status=400)
