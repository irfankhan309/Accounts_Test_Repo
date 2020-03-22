from django.urls import path
from TestApp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('secure',views.secure,name='secure'),
    path('profile',views.profile,name='profile'),
]
