from django.urls import path
from .views import ProjectListAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='projects-list'),
]
