from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from html import unescape
from html import escape
from .forms import *
from .models import *
import json
from django.core import serializers
from basket.models import *

# Create your views here.

def getUser(request):
    if 'login' in request.session:
        m_user = user.objects.get(nickname = request.session['login'])
        return m_user
    else: return None

class index(View):
    def get(self, request):
        yourposts = []
        if 'login' in request.session:
            m_user = user.objects.get(nickname = request.session['login'])
            yourposts = post.objects.filter(parent = None, user = m_user)
        return render(request, 'blog/main.html', context={
            'path' : request.get_full_path(),
            'postspublic' : post.objects.filter(parent = None, public=True),
            'yourposts' : yourposts,
        })

class ajaxAddPost(View):
    def post(self, request):
        m_user = user.objects.get(nickname = request.session['login'])
        newPost = PostAdd(request.POST, request.FILES)

        if newPost.is_valid():
            form = newPost.save(commit=False)
            form.user = m_user
            form.img = request.FILES['img']
            if request.POST['parent'] != 'None':
                form.parent = post.objects.get(id = request.POST['parent'])
            else:
                form.parent = None
            form.save()
        else:
            print(newPost.errors)
        return HttpResponse('Ура!')

class ajaxGetPostText(View):
    def post(self, request):
        postnow = post.objects.get(id = request.POST['id'])

        m_user = getUser(request)
        mass = {}

        if m_user:
            confirmUser = postnow.userConfirm(m_user)
            price = postnow.getPricedir()
            
            if confirmUser:
                mass.update({'text' : postnow.text})
                mass.update({'allow' : True})
            elif price == 0:
                mass.update({'text' : postnow.text})

        return HttpResponse(json.dumps(mass))

class ajaxDeletePost(View):
    def post(self, request):
        post.objects.get(id = request.POST['id']).delete()
        return HttpResponse('Готово')

class ajaxPublicationPost(View):
    def post(self, request):
        if 'login' in request.session:
            m_post = post.objects.get(id = request.POST['id'])
            if m_post.public == True:
                m_post.public = False
            else:
                m_post.public = True
            m_post.save(update_fields=["public"])
        return HttpResponse('Готово')

class ajaxGetDir(View):
    def post(self, request):
        m_post = 0
        m_posts = 0
        if request.POST['id'] != 'None':
            m_post = post.objects.get(id = request.POST['id'])
            m_posts = post.objects.filter(parent = m_post)
        else:
            m_posts = post.objects.filter(parent = None)

        if request.POST.get('public', None) == 'all':
            m_posts = m_posts.filter(public = True)
        else:
            m_user = user.objects.get(nickname = request.session['login'])
            m_posts = m_posts.filter(user = m_user)
        # print(m_posts[0].pricedir.all())
        data = serializers.serialize('json', m_posts)

        data2 = json.loads(data)
        for i in range(len(m_posts)):
            del data2[i]['fields']['text']
            data2[i]['fields']['pricedir'] = m_posts[i].getPricedir()
        data = json.dumps(data2)
        return HttpResponse(data)

class ajaxSavePost(View):
    def post(self, request):
        m_post = post.objects.get(id = request.POST['id'])
        m_post.text = request.POST['text']
        m_post.title = request.POST['title']
        m_post.price = request.POST['price']
        m_post.intro = request.POST['intro']
        m_post.save()
        return HttpResponse('Eeee')

class ajaxAddToBasket(View):
    def post(self, request):
        b = basket.objects.create(
            user = user.objects.get(nickname = request.session['login']),
            post_buy = post.objects.get(id = request.POST['id']),
        )
        return HttpResponse('Eeee')