from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User)
    body = models.TextField()

class Club(models.Model):
    name = models.CharField(max_length= 200)
    county = models.CharField(max_length= 200)
    location = models.URLField()
    province = models.CharField(max_length=50)
    
    def __str__(self):
        return self.county + " - " + self.name
        
    