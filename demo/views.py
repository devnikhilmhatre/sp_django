from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TestModel
from .seralizers import Ser
# Create your views here.

class TestView(APIView):
    def get(self, resuest):
        # test = TestModel.objects.raw('select * from demo_testmodel;') # normal query
        test = TestModel.objects.raw('call demo(5);')  # sp call
        ser = Ser(test, many=True)
        return Response(ser.data)