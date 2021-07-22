from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.urls import reverse

#from datetime import datetime,date

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class UserProfile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag=models.CharField(max_length=255, default="")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255, default="programming")
    likes=models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title+' | '+str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
# Create your models here.
