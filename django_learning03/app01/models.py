from django.db import models

# Create your models here.

class Classes(models.Model):
    """
    班级表,男
    """
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

class Teachers(models.Model):
    """
    老师表，女
    """
    name = models.CharField (max_length=32)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE,)

class UserInfo(models.Model):
    userid = models.CharField(max_length=20)
    userstatus = models.CharField(max_length=10)
    username = models.CharField(max_length=32)
    usercardnum = models.CharField(max_length=20)
    userage = models.IntegerField
    usergender = models.BooleanField
    userphone = models.CharField(max_length=15)
    useraddr = models.CharField(max_length=100)
