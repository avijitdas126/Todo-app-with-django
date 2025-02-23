import uuid 
from django.db import models
import time
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    date=models.DateField()
    is_completed = models.BooleanField(default=False)
    priority=models.IntegerField(default=0)
    time=models.TimeField()
    user_id= models.UUIDField(max_length=10,null=True)
    todo_id = models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=10)
    # other fields 

class User_Model(models.Model):
    name = models.CharField(max_length=255)
    avatar=models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    password=models.CharField(max_length=255)
    token_id= models.UUIDField(default=uuid.uuid4, primary_key=True,max_length=10)
    
