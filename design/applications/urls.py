from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.UserProfile, name='profile'),
    path('create/', views.CreateApplicationView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteApplicationView.as_view(), name='delete'),
]
