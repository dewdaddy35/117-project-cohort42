from django.urls import path
from content import views

urlpatterns = [
    path("", views.project_list, name= "project_list")
]