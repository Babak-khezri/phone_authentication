from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('verify/', views.verify_view, name='verify'),
]
