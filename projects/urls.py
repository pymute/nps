from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create-project/', views.create_project, name='create-project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete-project'),
    path('update-project/<str:pk>/', views.update_project, name='update-project'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
