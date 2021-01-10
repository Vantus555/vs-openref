from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from html import unescape
from html import escape
import os
from .forms import *
from .models import *

# Create your views here.

class index(View):
    def get(self, request):
        if 'login' in request.session:
            return render(request, 'user/admin.html', context={
                'path' : request.get_full_path(),
                'user' : user.objects.get(nickname = request.session['login'])
            })
        elif 'login' not in request.session and not request.GET.get('reg', False):
            return render(request, 'user/input.html', context={'path' : request.get_full_path()})
        elif request.GET.get('reg', None):
            return render(request, 'user/reg.html', context={'path' : request.get_full_path()})

class images(View):
    def get(self, request):
        return render(request, 'user/images.html', context={
            'path' : request.get_full_path(),
            'user' : user.objects.get(nickname = request.session['login'])
        })

class ajaxDeleteImage(View):
    def post(self, request):
        try:
            os.remove(request.POST['path'])
            return HttpResponse('Готово')
        except BaseException:
            return HttpResponse('Ошибка')

class ajaxRegistration(View):
    def post(self, request):
        post = request.POST
        print(post)
        form = RegistrationUserForm(request.POST)
        
        if form.is_valid():
            if post['confirmpass'] == post['password']:
                form.save()
                response = redirect('main_url')
                return HttpResponse('Готово!')
            else:
                return HttpResponse('Пароли не совпадают!')
        else:
            return HttpResponse(form.errors)

class ajaxInput(View):
    def post(self, request):
        post = request.POST
        form = InputUserForm(request.POST)

        if form.is_valid():
            # request.session.set_expiry(3600 * 24 * 30)
            request.session.set_expiry(3600 * 24 * 30)
            request.session['login'] = request.POST['nickname']
            return HttpResponse('Вход!')
        else:
            print(form.errors)
            return HttpResponse(form.errors)
            
class ajaxChangeMiniTag(View):
    def post(self, request):
        m_user = user.objects.get(nickname = request.session['login'])
        m_user.minitag = request.POST['minitag']
        m_user.save(update_fields=["minitag"])
        return HttpResponse()

class ajaxChangePass(View):
    def post(self, request):
        m_user = user.objects.get(nickname = request.session['login'])
        if m_user.password == request.POST['password']:
            m_user.password = request.POST['newpassword']
            m_user.save(update_fields=["password"])
            return HttpResponse('Готово!')
        else:
            return HttpResponse('Пароли не совпадают!')

''' ///////////////////////////////////////////////////////////////////// '''

class roles_and_roots(View):
    def get(self, request):
        if 'login' in request.session:
            return render(request, 'user/roles_and_roots.html', context={
                'path' : request.get_full_path(),
                'roles' : role.objects.all(),
                'roots' : freedom.objects.all(),
            })
        else:
            return redirect('main_url')

class ajaxAddRole(View):    
    def post(self, request):
        print(request.POST)
        newRole = AddRole(request.POST)

        if newRole.is_valid():
            newRole.save()
            return HttpResponse('Роль добавлена!')
        else:
            return HttpResponse('Такой ранк или роль уже существуют!')

class ajaxDeleteRole(View):
    def post(self, request):
        print(request.POST)
        removeRole = role.objects.get(id = request.POST['id']).delete()

        return HttpResponse('Роль удалена!')

class ajaxAddRoot(View):    
    def post(self, request):
        print(request.POST)
        newRoot = AddFreedom(request.POST)

        if newRoot.is_valid():
            newRoot.save()
            return HttpResponse('Право добавлено!')
        else:
            return HttpResponse('Такое право уже уже существуют!')

class ajaxUpdateRole(View):
    def post(self, request):
        # print(request.POST)
        m_role = role.objects.get(id = request.POST['roleid'])
        m_role.name = request.POST['rolename']
        m_role.settings = request.POST['rolesettings']
        m_role.save(update_fields=["name", 'settings'])

        add = request.POST['add'].split(',')
        remove = request.POST['remove'].split(',')
        for i in add:
            elem = freedom.objects.filter(name = i)
            if len(elem) == 1:
                m_role.freedoms.add(elem[0])
        for i in remove:
            elem = freedom.objects.filter(name = i)
            if len(elem) == 1:
                m_role.freedoms.remove(elem[0])

        return HttpResponse('Сохранено!')

class ajaxGetFreedoms(View):
    def post(self, request):
        if request.POST['id'] == '':
            return HttpResponse('Выберите роль!')
        else:
            m_freedoms = role.objects.get(id = request.POST['id']).freedoms.all()
            listfreedoms = []

            for i in m_freedoms:
                listfreedoms.append(i.name)

            return JsonResponse({'freedoms': list(listfreedoms)})

class ajaxUserExit(View):
    def post(self, request):
        if 'login' in request.session:
            request.session.flush()
            return HttpResponse('Выход!')
        else:
            return HttpResponse('Вы и не входили, чтобы выходить!')
