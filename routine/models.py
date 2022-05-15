from django.db import models
from account.models import MyUser

# Create your models here.

class routine(models.Model):
    routine_id = models.AutoField(primary_key=True)  
    account_id = models.ForeignKey(MyUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100, blank=True, null=True) 
    category = models.CharField(max_length=100, blank=True, null=True)  
    goal = models.CharField(max_length=100, blank=True, null=True) 
    is_alarm = models.BooleanField(default=False) 
    is_deleted = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


class routine_result(models.Model):
    routine_result_id = models.AutoField(primary_key=True) 
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    result = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    routine_day = models.CharField(max_length=100, blank=True, null=True)


class day(models.Model):
    day = models.CharField(max_length=50, blank=True, null=True)
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)