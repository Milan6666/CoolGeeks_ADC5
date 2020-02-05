from django.urls import path
from . import views 

app_name = 'uploaddownload'

urlpatterns = [
    path('uploadfiles/', views.uploadfiles, name="uploadfiles"),
    path('list_food/', views.list_food, name="list_food"),
    path('list_food/delete/<int:pk>/', views.delete_data, name="delete_data"),

]


