from django.contrib import admin
from django.urls import path, include
from app_to_do_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_to_do_list.urls')),
]
