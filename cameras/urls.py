from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('api/locations/', views.get_locations, name='get_locations'),
    path('api/add/', views.add_location, name='add_location'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
