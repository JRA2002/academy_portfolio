from django.contrib.auth.models import Group
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=Profile)
def add_user_to_students_group(sender,instance,created,**kwargs):
    if created:
        try:
            group1 = Group.objects.get(name='Student')
        except:
            group1 = Group.objects.create(name='Student')
            group2 = Group.objects.create(name='Professor')
            group3 = Group.objects.create(name='Helper')
            group4 = Group.objects.create(name='Administrative')
        instance.user.groups.add(group1)
