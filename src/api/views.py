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
        # parse grid data
        N = int(request.query_params.get('N'))
        grid_structure = request.query_params.get('grid')
        str_rows = grid_structure.split(' ')
        grid=[]
        for str_r in str_rows:
            row=[]
            for c in str_r:
                row.append(c)
            grid.append(row)

    except:
        return HttpResponse('Unknown request data', status=400)
    # save entry to db
    requestData = {'requestTime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                   'gridSize': N,
                   'gridStructure': grid_structure}
    db.push(requestData)

    # find the path
    res = maze_utils.mario_save_princess(N, grid)
    return HttpResponse(json.dumps(res))
