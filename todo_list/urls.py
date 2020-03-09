from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('un_cross/<list_id>', views.un_cross, name="un_cross"),
    path('edit/<list_id>', views.edit, name="edit"),
]
