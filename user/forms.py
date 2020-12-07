from django import forms
from .models import *
from django.core.exceptions import ValidationError

class RegistrationUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['nickname', 'email', 'password'] # '__all__'
        
    def clean_nickname(self):
        m_nickname = self.cleaned_data["nickname"]
        if user.objects.filter(nickname__iexact=m_nickname).count():
            raise ValidationError('Такое имя уже существует!')
        return m_nickname

    def clean_email(self):
        m_email = self.cleaned_data["email"]
        if user.objects.filter(email__iexact = m_email).count():
            raise ValidationError('Такой email уже существует!')
        return m_email

    def save(self):
        m_user = user.objects.create(
            nickname = self.cleaned_data['nickname'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password'],
        )
        return m_user

class InputUserForm(forms.Form):
    nickname = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)

    def clean_nickname(self):
        m_nickname = self.cleaned_data["nickname"]
        if user.objects.filter(nickname__iexact=m_nickname).count() == 0:
            raise ValidationError('Такой пользователь не существует!')
        return self.cleaned_data["nickname"]

    def clean_password(self):
        if self.cleaned_data.get('nickname', None):
            m_nickname = self.cleaned_data["nickname"]
            m_password = user.objects.filter(nickname__iexact = m_nickname)
            if m_password.count() != 0:
                for m_user in m_password:
                    if m_user.password != self.cleaned_data["password"]:
                        raise ValidationError('Неправильный пароль!')
        return self.cleaned_data["password"]

class AddRole(forms.ModelForm):
    class Meta:
        model = role
        fields = '__all__'

    def save(self):
        m_role = role.objects.create(
            name = self.cleaned_data['name']
        )
        return m_role

class AddFreedom(forms.ModelForm):
    class Meta:
        model = freedom
        fields = '__all__'

    def save(self):
        m_role = freedom.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description']
        )
        return m_role