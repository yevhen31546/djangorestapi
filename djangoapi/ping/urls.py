from django.urls import path
from .views import *

urlpatterns = [
    path('ping/', HelloView.as_view(), name='ping'),
]