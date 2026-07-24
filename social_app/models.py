from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    image = CloudinaryField("image",null=True)
    bio = models.TextField(blank=True)


class Tags(models.Model):
    tags = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tags
    

class Posts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    caption = models.TextField(null=False,blank=False)
    image = CloudinaryField(resource_type="auto",null=True,blank=True)
    location = models.CharField(max_length=50,blank=True)
    visibility = models.CharField(max_length=50,default="Public")
    tags = models.ManyToManyField(Tags,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    parent = models.ForeignKey("self",null=True,blank=True,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,related_name="like")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["user","post"],
                name="unique_post_like"
            )
        ]

class Followers(models.Model):
    follower = models.ForeignKey(CustomUser, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser,related_name="followers",on_delete=models.CASCADE)
    follow_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower","following"],
                name="unique_follow"
            )
        ]

class Notifications(models.Model):
    user = models.ForeignKey(CustomUser, related_name="notifications", on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser,related_name="sent_notifications", on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,related_name="notifications", on_delete=models.CASCADE)
    notify_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)



