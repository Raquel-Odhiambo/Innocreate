from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField( default=False)
    is_lecturer = models.BooleanField( default=False)
    admission_number = models.CharField(max_length=200, null = True, blank = True)
    employment_no = models.CharField(max_length=200, null = True, blank = True)
    category= models.CharField(max_length=50,null = True, blank = True ,choices=(
        ('computer_science department','Computer_Science Department'),
        ('computer_technology department','Computer_Technology Department'),
        ('information_technology deaprtment','Information_Technology Department')

        ))

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return str(self.user)

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    

    def __str__(self):
         return str(self.user)

class Project(models.Model):
    STATUS_CHOICES = (
        ("ongoing", "Ongoing"),
        ("complete", "Complete"),
        ("pending", "Pending")

    )

    title = models.CharField(max_length = 300)
    project_description = models.TextField(null =True, blank = True) #remove null and blank
    project_category = models.CharField(max_length= 100, default = 'Software') #remove default
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')
    supervisor = models.ForeignKey(User, on_delete = models.CASCADE)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_projects')
    document = models.FileField(upload_to = 'documents/')
    # inchurge = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_projs', blank = True,null = True)

    
class Comm(models.Model):
    subject = models.CharField(max_length = 100)
    mess = models.TextField()
    created_time = models.DateTimeField(datetime.now())
    approved = models.BooleanField(default = False)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    lec = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'my_messages')
   

    def __str__(self):
         return self.subject

class reply(models.Model):
    mess = models.TextField()
    created_time = models.DateTimeField(datetime.now())
    mess = models.ForeignKey(Comm, on_delete = models.CASCADE)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
         return str(self.id)