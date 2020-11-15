from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class index(View):
    def get(self, request):
        if 'login' not in request.session and not request.GET.get('reg', False):
            return render(request, 'user/input.html', context={'path' : request.get_full_path()})
        elif request.GET.get('reg', None):
            return render(request, 'user/reg.html', context={'path' : request.get_full_path()})