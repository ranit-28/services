from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class project_serializer(serializers.ModelSerializer):
    user=user_serializer(many=True,read_only=True)

    class Meta:
        model=project
        fields=['id','project_name','clients','created_by','created_at','user']

class client_serializer(serializers.ModelSerializer):
    projects=project_serializer(many=True,read_only=True)
    created_by=serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model=client
        fields=['id','client_name','created_by','created_at','updated_at','projects']

class create_project_serializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model=project
        fields=['project_name','user']
