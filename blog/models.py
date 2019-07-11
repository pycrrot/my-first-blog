from django.db import models
from django.utils import timezone
#real django korea girls project have so many problem like this insincere explains

##django

##django.db #django's database import
##django.db.models -> django.db.(models.Model)

##django.utils #import django's utils
##django.utils.timezone #this is one of django's utils packages
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)#restrict string length like title
    text=models.TextField()#textfield long text string
    created_date=models.DateTimeField(default=timezone.now)#configure time
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
    def _str_(self):
        return self.title

# Post is model's name
# if you want to know specifically, come on this link https://docs.djangoproject.com
# Create your models here.

# Last exectue like this python manage.py makemigrations blog in command line interface
# and then python manage.py migrate blog
