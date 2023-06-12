from django.urls import path,include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.loginout, name='logout'),
]