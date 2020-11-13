from django.urls import path
from . import views
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path(r'test', views.test_api, name='test_api_communication')
]