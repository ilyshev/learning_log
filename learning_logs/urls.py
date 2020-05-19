'''Defining URL schemes for learning_logs'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
	#Home page
	path('', views.index, name='index'),
	#Page with List of all themes
	path('topics/', views.topics, name='topics'),
	#Page with information about choosing theme
	path('topics/<int:topic_id>/', views.topic, name='topic')
]
