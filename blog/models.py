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

# class PriceDirManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(parent = self.id)

class post(models.Model):
    img = models.ImageField(upload_to = upload_to, null=True, blank = True, unique = True)
    title = models.CharField(max_length = 100)
    intro = models.CharField(max_length = 300, blank=True)
    text = models.JSONField(blank=True, null=True, default="[]")
    creation_data = models.DateTimeField(auto_now_add = True)
    data_last_child = models.DateTimeField(auto_now_add = True)
    type = models.CharField(max_length = 30, choices=TYPE_PAPER)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    parent = models.ForeignKey('post', on_delete = models.CASCADE, null=True, blank = True)
    public = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank = True)
    pricedir = models.FloatField(null=True, blank = True)
    # objects = models.Manager()
    # pricedir = PriceDirManager()

    def getPricedir(self):
        price = 0
        if self.type == 'Папка':
            postInDir = post.objects.filter(parent = self)
            for i in postInDir:
                price += i.getPricedir()
        else: price += self.price
        return price
    
    def userConfirm(self, m_user):
        if m_user == self.user:
            return True
        
        return False


    def __str__(self):
        return self.title

    def data(self):
        return '{}'.format(self.creation_data.astimezone(tz).strftime('%d.%m.%Y, %H:%M'))