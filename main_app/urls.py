from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Message Routes
    path('messages/new/', views.new_message, name='new_message')
]
