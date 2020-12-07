from django.db import models
from user.models import *
from django.utils import timezone
tz = timezone.get_default_timezone()

# Create your models here.

TYPE_PAPER = (
        ('Папка', 'Папка'),
        ('Файл', 'Файл'),
    )

def upload_to(instance, filename):
    print(instance)
    return 'images/{username}/{filename}'.format(username=instance.user, filename=filename)

class post(models.Model):
    img = models.ImageField(upload_to = upload_to, null=True, blank = True, unique = True)
    title = models.CharField(max_length = 100)
    intro = models.CharField(max_length = 300, blank=True)
    text = models.TextField(blank=True)
    creation_data = models.DateTimeField(auto_now_add = True)
    data_last_child = models.DateTimeField(auto_now_add = True)
    type = models.CharField(max_length = 30, choices=TYPE_PAPER)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    parent = models.ForeignKey('post', on_delete = models.CASCADE, null=True, blank = True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def data(self):
        return '{}'.format(self.creation_data.astimezone(tz).strftime('%d.%m.%Y %H:%M'))