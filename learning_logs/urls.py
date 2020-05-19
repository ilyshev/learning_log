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
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#Page for adding new theme
	path('new_topic/', views.new_topic, name='new_topic'),
	#Page for adding new enrty
	path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	#Page for editing entries
	path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
