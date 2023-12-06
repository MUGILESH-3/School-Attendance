from django.db import models

# Create your models here.

class userregister(models.Model):
    Name=models.CharField(max_length=20,default=" ")
    Rollno=models.IntegerField(default=" ")
    Username=models.CharField(max_length=20,default=" ")
    Password=models.IntegerField(default=" ")

    class Meta:
        db_table='user'
   


class attendance(models.Model):
    Name=models.CharField(max_length=25,default=" ")
    Rollno=models.IntegerField(default=" ")
    Date=models.DateField(default=" ")

    class Meta:
        db_table='stud_attendance'