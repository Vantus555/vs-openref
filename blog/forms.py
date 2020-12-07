from django import forms
from .models import *
from django.core.exceptions import ValidationError

class PostAdd(forms.ModelForm):
    class Meta:
        model = post
        exclude = ("user",'parent')
        
    def clean_img(self):
        pass
        # m_nickname = self.cleaned_data["nickname"]
        # if user.objects.filter(nickname__iexact=m_nickname).count():
        #     raise ValidationError('Такое имя уже существует!')
        # return m_nickname

    # def save(self):
    #     m_user = user.objects.create(
    #         nickname = self.cleaned_data['nickname'],
    #         email = self.cleaned_data['email'],
    #         password = self.cleaned_data['password'],
    #     )
    #     return m_user