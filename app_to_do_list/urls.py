from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('list/<list_id>/', views.list, name=""),
    path('item/<item_id>/delete/', views.remove_item, name='remove_item'),
    path('cross/<item_id>', views.cross_item, name='cross_item'),
    path('cross_off/<item_id>', views.cross_off_item, name='cross_off_item'),
    path('edit_item/<item_id>', views.edit_item, name='edit_item'),
]
