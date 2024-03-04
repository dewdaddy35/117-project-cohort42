from django.urls import path
from content import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.project_list, name= "project_list"),
    path("project_new", views.project_new, name='project_new'),
    path("experience_list/", views.experience_list, name="experience_list"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)