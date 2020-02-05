from django.urls import path,include
from . import views
app_name='user_registration'
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='home'),
    path('aboutUs/',views.aboutUs,name='aboutUs'),

]
