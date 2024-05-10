from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='users/default_user.jpg',upload_to='users/')
    address = models.CharField(max_length=40,null=True,blank=True)
    location = models.CharField(max_length=40,null=True,blank=True)
    telephone = models.CharField(max_length=9,null=True,blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile, sender=User)
