from django.urls import NoReverseMatch, reverse
from django.urls import path
from blog import views

app_name='blog'


urlpatterns=[
	path('',views.blog_index, name='blog_index'),
	path('<int:pk>/',views.blog_detail, name='blog_detail'),
	path('<category>/', views.blog_category, name='blog_category'),


]