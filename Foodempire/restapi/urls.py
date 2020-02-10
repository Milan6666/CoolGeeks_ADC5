from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "restapi"

urlpatterns = [
    path('api/', views.api_data, name="api_data"),
    path('api/<int:pk>/', views.api_spec_data, name="api_spec_data"),
    path('api/add', views.api_add, name="api_add"),
    path('api/update/<int:pk>', views.api_update_data, name="api_update_data"),
    path('api/delete/<int:pk>', views.api_delete_data, name="api_delete_data"),
    path('list_food/pagination/<int:PAGENO>', views.list_food_pagination, name='list_food_pagination'),
 ]