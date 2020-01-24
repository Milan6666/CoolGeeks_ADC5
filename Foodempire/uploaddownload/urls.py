from django.urls import path
from . import views 

app_name = 'uploaddownload'

urlpatterns = [
    path('upload/', views.uploadfiles, name="uploadfiles"),
    path('listfood/', views.list_food, name="list_food"),
    path('listfood/delete/<int:pk>/', views.delete_data, name="delete_data"),

]


