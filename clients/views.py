from django.shortcuts import render
from .models import *
from .serializers import *
# from rest_framework import generics,permissions
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.
 
class create_clinets(ListCreateAPIView):
    queryset=client.objects.all()
    serializer_class=client_serializer
    permission_classes=[IsAuthenticated]


class client_details(RetrieveUpdateDestroyAPIView):
    queryset=client.objects.all()
    serializer_class=client_serializer
    permission_classes=[IsAuthenticated]

class create_project(CreateAPIView):
    queryset=project.objects.all()
    serializer_class=create_project_serializer
    permission_classes=[IsAuthenticated]

    def create(self,serializer):
        client_id=self.kwargs.get('client_id')
        clients=client.objects.get(id=client_id)
        serializer.save(clients=clients,created_by=self.request.user)
        

class project_view(APIView):
    permission_classes=[IsAuthenticated]
    

    def get(self,request,format=None):
        projects=project.objects.all()
        serializer=project_serializer(projects,many=True)
        return Response(serializer.data)
    
