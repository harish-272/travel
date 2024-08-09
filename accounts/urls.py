from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout, name = 'logout'),
    path('contact',views.contact, name = 'contact'),
    path('destination/<int:dest_id>/', views.destination_detail, name='destination_detail'),
    path('index',views.index, name='index')
] 