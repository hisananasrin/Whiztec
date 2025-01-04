from django.urls import path
from .import views
from django.shortcuts import render 
 
urlpatterns = [
    path('', views.task_list, name='tasklist'),
    path('create/', views.task_create, name='taskcreate'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    # path('calendar/', views.calendar_view, name='calendar_data'),
    # path('calendar/view/', lambda request: render(request, 'calendar.html'), name='calendar_view'),
    
    ]

