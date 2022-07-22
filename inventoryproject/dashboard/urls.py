from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='staff'),
    path('recipe/', views.recipe, name='recipe')
]
