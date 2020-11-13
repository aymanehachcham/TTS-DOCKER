from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
@never_cache
def test_api(request):
    return Response({'response':"You are successfully connected to the TTS API"})