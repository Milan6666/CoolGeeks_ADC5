from django.urls import path
from . import views 

app_name = 'uploaddownload'

urlpatterns = [
    path('uploadfiles/', views.uploadfiles, name="uploadfiles"),
    path('list_food/', views.list_food, name="list_food"),
    path('list_food/pagination/<int:PAGENO>', views.list_food_pagination, name='list_food_pagination'),
    path('list_food/delete/<int:pk>/', views.delete_data, name="delete_data"),

]


