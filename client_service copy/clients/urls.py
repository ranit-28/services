from django.urls import path
from .views import *

urlpatterns = [
    path('create_client',create_clinets.as_view(),name='create_clients'),
    path('client_details',client_details.as_view(),name='client_detail'),
    path('client_details/<int:pk>',client_details.as_view(),name='client_details'),
    path('create_project',create_project.as_view(),name='create_project'),
    path('project_view',project_view.as_view(),name='project_view'),
]
