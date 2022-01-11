from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects),
    path('project/<str:pk>/', views.single_project)
]