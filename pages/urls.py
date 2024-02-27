from django.urls import path
from pages.views import home, project, experience, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('project/', project, name='project'),
    path('experience/', experience, name='experience'),
    path('contact_view/', contact_view, name='contact'),
]