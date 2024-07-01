from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class client(models.Model):
    client_name=models.CharField(max_length=225)
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='client')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class project(models.Model):
    project_name=models.CharField(max_length=225)
    clients=models.ForeignKey(client,on_delete=models.CASCADE,null=True,related_name='projects')
    users=models.ManyToManyField(User,related_name='user_project')
    created_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='Projects_created')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name