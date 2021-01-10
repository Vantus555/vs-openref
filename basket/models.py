from django.db import models
from user.models import *
from blog.models import *

# Create your models here.

class basket(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    post_buy = models.ForeignKey(post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "post_buy")