from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('list/<list_id>/', views.list, name="list_page"),
    path('list/<list_id>/delete/', views.remove_list, name='remove_list'),
    path('list/<list_id>/list_item/', views.edit_list, name='edit_list'),
    path('item/<item_id>/delete/', views.remove_item, name='remove_item'),
    path('item/<item_id>/cross/', views.cross_item, name='cross_item'),
    path('item/<item_id>/cross_off/', views.cross_off_item, name='cross_off_item'),
    path('item/<item_id>/edit_item/', views.edit_item, name='edit_item'),
]
