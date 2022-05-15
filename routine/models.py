from django.db import models
from account.models import MyUser

# Create your models here.

class routine(models.Model):
    routine_id = models.CharField(primary_key=True, max_length=30)  
    account_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='account_id') 
    title = models.CharField(max_length=100, blank=True, null=True) 
    category = models.CharField(max_length=100, blank=True, null=True)  
    goal = models.CharField(max_length=100, blank=True, null=True) 
    is_alarm = models.BooleanField(default=False) 
    is_deleted = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


class routine_result(models.Model):
    routine_result_id = models.CharField(primary_key=True, max_length=30) 
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    result = models.CharField(max_length=100, blank=True, null=True) 
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    routine_day = models.CharField(max_length=100, blank=True, null=True)


class day(models.Model):
    routine_id = models.ForeignKey(routine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)