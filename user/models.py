from django.db import models

# Create your models here.

def upload_to(instance, filename):
    print(instance)
    return 'images/{username}/{filename}'.format(username=instance, filename=filename)

class user(models.Model):
    img = models.ImageField(upload_to = upload_to, null=True, blank = True, unique = True)
    nickname = models.CharField(max_length = 50, blank=True, unique = True)
    minitag = models.CharField(max_length = 50, blank=True, unique = True)
    email = models.EmailField(max_length = 50, unique = True)
    password = models.CharField(max_length = 50)
    data = models.DateTimeField(auto_now_add = True)
    roles = models.ManyToManyField('role', blank=True, related_name='roles')
    # collabrators = models.ManyToManyField('collaborator', blank=True, related_name='collabrators')
    # buys = models.ManyToManyField('buy', blank=True, related_name='buys')

    def __str__(self):
        return self.nickname

    def get(self):
        arr = [self.nickname, self.email,  self.password, self.time()]
        return arr

    def getAll(self):
        arr = [self.nickname, self.email,  self.password, self.time(), self.roles.all()]
        return arr
    
    def time(self):
        return self.data.strftime('%d.%m.%Y %H:%M')
    
    def getRoles(self):
        return self.roles.all()

    def getRolesArray(self):
        arr = set()
        current = self.roles.all()
        for rol in current:
            arr.add(rol.name)
        return arr

    def getFreedoms(self):
        arr = set()
        roles = self.getRoles()
        for i in roles:
            freedoms = i.freedoms.all()
            for free in freedoms:
                arr.add(free.name)
        return arr

class role(models.Model):
    name = models.CharField(max_length=50)
    settings = models.CharField(max_length=50, blank=True)
    freedoms = models.ManyToManyField('freedom', blank=True, related_name='freedoms')

    def __str__(self):
        return self.name

class freedom(models.Model):
    name = models.CharField(max_length=50, unique = True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class collaborator(models.Model):
#     name = models.CharField(max_length=50)
#     access = models.IntegerField(default=0)

# class buy(models.Model):
#     name = models.CharField(max_length=50, unique = True)
#     user = models.CharField(max_length=50, unique = True)