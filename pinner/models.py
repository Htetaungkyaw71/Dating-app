from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
# Create your models here.

class User(AbstractUser):
    pass




class Passion(models.Model):
    name = models.CharField(max_length=64)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="pp")
    birth = models.IntegerField()
    user_gender = models.CharField(max_length=64)
    like_gender = models.CharField(max_length=64)
    interest = models.CharField(max_length=64)
    height = models.IntegerField()
    image = models.ImageField(null=False,blank=False)
    passions = models.ManyToManyField(Passion,blank=False,related_name="p")
    location = models.FloatField(blank=True,null=True)
    liked = models.ManyToManyField(User,blank=True,related_name="liker")
    unliked = models.ManyToManyField(User,blank=True,related_name="n")
    active = models.BooleanField(default=False)


    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "user_gender": self.user_gender,
            "like_gender": self.like_gender,
            "interest": self.interest,
            "height": self.height,
            "image": self.image,
            "passions": self.passions,
            "location": self.location,
        }

class SendMessage(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="s")
    message = models.CharField(max_length=64)
    receiver = models.ForeignKey(Profile,on_delete=models.Case,related_name="r")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.message}"




    
