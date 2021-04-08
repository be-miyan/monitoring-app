from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'
urlpatterns = [
    # ex: /dashboard/
    path('', views.IndexView, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('home/', views.HomeView.as_view(), name='home'),
    path('home/<str:period>/', views.HomeView.as_view(), name='home'),
] 

