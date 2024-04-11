from django.urls import path
from . import views

urlpatterns=[
    path('student/create/', views.student_view, name="student_create_url"),
    path('student/retrieve/', views.student_retrive_view, name="student_retrieve_url"),
     path('student/delete/', views.student_delete_view, name="student_delete_url"),
    path('student/retriev/spe/', views.student_sp_retrieve, name="student_sp_retrieve_url"),
    path('homepage', views.home, name="home_url")
]
