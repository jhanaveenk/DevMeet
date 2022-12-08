from django.urls import path
from . import views

urlpatterns = [
   path('', views.profiles, name="profilies"),
   path('profile/<str:pk>/', views.userProfile, name="user-profile"),
]