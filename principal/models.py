from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    professor = models.ForeignKey(User,limit_choices_to={'groups__name':'Professor'},on_delete=models.CASCADE) 
    class_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,related_name='student_registration',limit_choices_to={'groups__name':'Student'},on_delete=models.CASCADE)
    enable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.student.username} - {self.course.name}'
    
class Attendance(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,related_name='attendance',limit_choices_to={'groups__name':'Student'},on_delete=models.CASCADE)
    present = models.BooleanField(default=False,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    

    def __str__(self):
        return f'asistenace : {self.id}'
    
class Mark(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,related_name='marks',limit_choices_to={'groups__name':'Student'},on_delete=models.CASCADE)
    mark1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    mark2 = models.PositiveIntegerField(default=0,null=True,blank=True)
    mark3 = models.PositiveIntegerField(default=0,null=True,blank=True)
    Average = models.DecimalField(max_digits=3,decimal_places=1,null=True,blank=True)
    def __str__(self):
        return str(self.course)
    
