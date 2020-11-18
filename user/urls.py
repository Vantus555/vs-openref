from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', index.as_view(), name="user_url"),
    path('roles_and_roots', roles_and_roots.as_view(), name="roles_and_roots_url"),
]