from django.http import HttpResponse
from rest_framework.utils import json

from .utils import maze_utils
from rest_framework.decorators import api_view
import pyrebase
from datetime import datetime

firebaseConfig = {
    'apiKey': "AIzaSyAgYhkC1RCevNMpfAOOc8av0YZu6UGE144",
    'authDomain': "prestacap-5c95b.firebaseapp.com",
    'databaseURL': 'https://prestacap-5c95b-default-rtdb.europe-west1.firebasedatabase.app/',
    'projectId': "prestacap-5c95b",
    'storageBucket': "prestacap-5c95b.appspot.com",
    'messagingSenderId': "809839787928",
    'appId': "1:809839787928:web:73bb48d1dbc3c8b83ef5ed"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


@api_view(['GET'])
def maze_view(request):
    try:
        N = request.data.get('N')
        grid = request.data.get('grid')

        # TODO: remove
        N = 3
        grid = ['--m', '-x-', '-p-']
    except:
        return HttpResponse('Unknown request data', status=400)
    # save entry to db
    requestData = {'requestTime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   'gridSize': N,
                   'gridStructure': ';'.join(grid)}
    db.push(requestData)

    # find the path
    res = maze_utils.mario_save_princess(N, grid)
    return HttpResponse(json.dumps(res))
