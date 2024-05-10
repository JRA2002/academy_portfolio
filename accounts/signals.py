from django.contrib.auth.models import Group
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=Profile)
def add_user_to_students_group(sender,instance,created,**kwargs):
    if created:
        try:
            students = Group.objects.get(name='Student')
        except:
            students = Group.objects.create(name='Student')
            students = Group.objects.create(name='Professor')
            students = Group.objects.create(name='Helper')
            students = Group.objects.create(name='Adminitrative')
        instance.user.groups.add(students)
