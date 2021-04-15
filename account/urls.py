from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('verify/', views.verify_view, name='verify'),
]
