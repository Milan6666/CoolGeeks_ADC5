from django.urls import path,include
from . import views
app_name='user_registration'
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('profile/done',views.update_completed,name='profile_completed'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('aboutUs/',views.aboutUs,name='aboutUs'),
    path('profile/',views.user_profile,name='user_profile'),
]
