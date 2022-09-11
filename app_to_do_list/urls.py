from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.remove, name='remove'),
    path('cross/<list_id>', views.cross, name='cross'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('edit_item/<list_id>', views.edit_item, name='edit_item'),
]
