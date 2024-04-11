from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length=30)
    session = models.CharField(max_length= 15)
    university = models.CharField(max_length= 50)
    mobile_no = models.CharField(max_length = 12)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"