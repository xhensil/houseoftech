from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from django.utils import translation

# Create your models here.


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  slug =   models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  content = models.TextField()
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

class Contact(models.Model):
 name=models.CharField(max_length=30, null=True, blank=True)
 email=models.EmailField(null=True, blank=True)
 message=models.TextField(max_length=1000, null=True, blank=True)
def __str__(self):
  return self.name