from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from html import unescape
from html import escape
from .models import *
import json
from django.core import serializers
from user.models import *
from .models import *

# Create your views here.

class basketView(View):
    def get(self, request):
        m_user = user.objects.get(nickname = request.session['login'])
        m_basket = basket.objects.filter(user = m_user)
        return render(request, 'basket/index.html', {
            'baskets': m_basket
        })