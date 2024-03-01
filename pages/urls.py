from django.urls import path
from pages.views import home, experience, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('experience/', experience, name='experience'),
    path('contact_view/', contact_view, name='contact'),
]