from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view_timetable, name='view_timetable'),  # Changed to 'view_timetable'
    path('subjects/add/', views.SubjectCreateView.as_view(), name='add_subject'),
    path('faculty/add/', views.FacultyCreateView.as_view(), name='add_faculty'),
    path('generate/', views.generate_timetable, name='generate_timetable'),  # Changed to 'generate_timetable'
]
