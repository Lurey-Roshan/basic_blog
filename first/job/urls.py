from django.urls import path
from job import views

app_name='job'

urlpatterns=[
	path('',views.job_index, name='job_index'),
	path('<int:pk>/', views.job_detail, name='job_detail'),


]