from django.urls import path
from . import views

app_name = 'banking_app'

urlpatterns = [
    path('countries/', views.country_list, name='country_list'),
    path('countries/create/', views.country_create, name='country_create'),
    path('countries/<int:pk>/edit/', views.country_edit, name='country_edit'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),
]
