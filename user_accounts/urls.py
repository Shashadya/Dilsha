from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.logout_user, name='logout_user'),

]
