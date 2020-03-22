from django.urls import path,include
from Accounts import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('Login',views.Login_view,name='Login'),
    path('logout',views.logout,name='logout'),
]
