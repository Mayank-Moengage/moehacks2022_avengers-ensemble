from curses.ascii import HT
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Test
from .serializers import TestSerializer
# Create your views here.
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
def test_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            t = Test.objects.get(id=id)
            serializer = TestSerializer(data=t)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
    
    res = Test.objects.all()
    serializer = TestSerializer(data=res)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')