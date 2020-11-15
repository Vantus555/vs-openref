from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', index.as_view(), name="user_url"),
]