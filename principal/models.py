from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver

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
    enable = models.BooleanField(default=True,verbose_name='Regular')

    def __str__(self):
        return f'{self.student.username} - {self.course.name}'
    
class Attendance(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,related_name='attendance',limit_choices_to={'groups__name':'Student'},on_delete=models.CASCADE)
    present = models.BooleanField(default=False,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    

    def __str__(self):
        return f'asistance : {self.id}'
    
    def update_registration_status_enable(self):
        course_instance = Course.objects.get(id=self.course.id)
        total_classes = course_instance.class_quantity
        total_absens = Attendance.objects.filter(student=self.student,course=self.course,present=False).count()
        absens_percentaje = (total_absens/total_classes)*100

        registration = Registration.objects.get(course=self.course, student=self.student)

        if absens_percentaje > 20:
            registration.enable = False
        else:
            registration.enable = True
        registration.save()

        
    
class Mark(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,related_name='marks',limit_choices_to={'groups__name':'Student'},on_delete=models.CASCADE)
    mark1 = models.PositiveIntegerField(default=0,null=True,blank=True)
    mark2 = models.PositiveIntegerField(default=0,null=True,blank=True)
    mark3 = models.PositiveIntegerField(default=0,null=True,blank=True)
    average = models.DecimalField(max_digits=3,decimal_places=1,null=True,blank=True)
    def __str__(self):
        return str(self.course)
    
    def calculate_average(self):
        marks = [self.mark1,self.mark2,self.mark3]
        valid_marks = [mark for mark in marks if mark is not None]
        if valid_marks:
            return sum(valid_marks)/len(valid_marks)
        return None
    
    def save(self, *args, **kwargs):
        #verify if some mark change
        if self.mark1 or self.mark2 or self.mark3:
            self.average = self.calculate_average() #calculate an average and call a function
        super().save(*args,**kwargs) #save data

@receiver(post_save,sender=Attendance)
@receiver(post_delete, sender=Attendance)
def update_registration_status_enable(sender,instance,**kwargs):
    instance.update_registration_status_enable()

