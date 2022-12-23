from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    year=models.CharField(max_length=10,default=None,null=True,blank=True)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)
    address=models.TextField()
    gender=models.CharField(max_length=6,null=True)
    image=models.ImageField(upload_to='newimages/')

    def is_exists(self):
        if Student.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_data_by_email(mail):
        return Student.objects.get(email=mail)
class Teacher(models.Model):
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=50)
    qualification=models.CharField(max_length=30,default='Not define')
    address=models.TextField()
    gender=models.CharField(max_length=6,null=True)
    contact=models.IntegerField(max_length=10,default=None,null=True,blank=True)
    image=models.ImageField(upload_to='newimages/')

    def is_exists(self):
        if Teacher.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_data_by_email(mail):
        return Teacher.objects.get(email=mail)

class Course(models.Model):
    course=models.CharField(max_length=50)
    image=models.ImageField(upload_to='newimages/')
class Teachers(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=50)
    image=models.ImageField()
class Gall(models.Model):
    desc=models.CharField(max_length=15)
    image=models.ImageField(upload_to='newimages/')

class Content(models.Model):
    name=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    content=models.FileField(upload_to='newimages/',null=True,default=None)