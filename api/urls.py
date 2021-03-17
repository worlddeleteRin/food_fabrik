
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    # api requests here,
    path('get_products', views.api_get_allproducts, name='api_get_allproducts'),
    path('get_categories', views.api_get_allcategories, name='api_get_allcategories'),
    path('get_stocks', views.get_stocks, name='get_stocks'),
    path('check_account_exist', views.check_account_exist, name='check_account_exist'),
    path('auth_user', views.auth_user, name='auth_user'),
    path('register_user_request', views.register_user_request, name='register_user_request'),
    path('register_user_finish', views.register_user_finish, name='register_user_finish'),
    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('get_user_info', views.get_user_info, name='get_user_info'),
    path('get_user_orders', views.get_user_orders, name='get_user_orders'),
    path('get_user_addresses', views.get_user_addresses, name='get_user_addresses'),
    path('delete_user_address', views.delete_user_address, name='delete_user_address'),
    path('create_user_address', views.create_user_address, name='create_user_address'),
    path('change_user_password', views.change_user_password, name='change_user_password'),
]