from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin_dashboard, name='admin_page'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('user/', views.user_page, name='user_page'),
]
