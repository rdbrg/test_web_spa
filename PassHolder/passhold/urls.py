from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('update_data/<str:pk>/', views.update_data, name='edit'),
    path('delete_data/<str:pk>/', views.delete_data, name='delete'),
]
