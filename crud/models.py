from django.db import models
class form1(models.Model):

    
    name=models.CharField(max_length=200)
    rollno=models.IntegerField()
    phone=models.IntegerField()

# Create your models here.
