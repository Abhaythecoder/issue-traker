from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('project/<int:pk>/new_issue/', views.create_issue, name='create_issue'),
    path('project/new/', views.create_project, name='create_project'),
    path('issue/<int:issue_id>/toggle/',
         views.toggle_issue, name='toggle_issue'),
    path('issue/<int:issue_id>/delete/',
         views.delete_issue, name='delete_issue'),
]
