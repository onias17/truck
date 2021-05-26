from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Message Routes
    path('messages/new/', views.add_message, name='add_message'),
]
