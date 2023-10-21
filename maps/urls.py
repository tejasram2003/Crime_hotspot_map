from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('update_marker_coordinates',views.update_marker_coordinates,name='update_marker_coordinates'),
    path('history_dashboard/<str:latitude>/<str:longitude>/', views.history_dashboard, name='history_dashboard_with_name'),
    path('history_dashboard',views.history_dashboard,name='history_dashboard'),
    path('create_database',views.create_database,name='create_database'),
]
