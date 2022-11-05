from django.contrib import admin
from django.urls import path, include
# from django.http import HttpRespons

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]
