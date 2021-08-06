import pandas as pd
import numpy as np

import os
import django
from django.conf import settings
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_fabrik.settings')
django.setup()

from datetime import datetime

from users.models import * 
from cart.models import * 
from products.models import * 

def get_orders_by_time(time):
    date = datetime.fromtimestamp(time)
    # get all orders made in passed time
    orders = Order.objects.filter(created_at__gte = date)
    return orders
def get_orders_stat(time):
    orders_stat = {}
    orders = get_orders_by_time(time)
    # get orders count
    orders_stat['orders_count'] = orders.count()
    # get orders completed count
    orders_stat['orders_completed'] = orders.filter(status = 'completed').count()
    # get orders cancelled count
    orders_stat['orders_cancelled'] = orders.filter(status = 'cancelled').count()
    # get orders app count
    orders_stat['orders_mobile_count'] = orders.filter(order_source = 'mobile').count()
    # get orders site count
    orders_stat['orders_site_count'] = orders.filter(order_source = 'site').count()
    # get orders cash summary
    orders_amount = 0
    for order in orders:
        if order.status == 'completed':
            orders_amount += order.amount
    orders_stat['orders_amount'] = orders_amount
        
    return orders_stat


def get_users_by_time(time):
    date = datetime.fromtimestamp(time)
    # get all users registered in passed time
    users = User.objects.filter(created_at__gte = date)
    return users

def get_users_stat(time):
    # get users, registered by passed time
    users = get_users_by_time(time)
    users_stat = {}
    # get users registered count
    users_stat['users_registered'] = users.count()
    return users_stat

def get_all_info():
    time = int(input("Set time to scan"))
    # get all necessary stat
    orders_stat = get_orders_stat(time) 
    users_stat = get_users_stat(time)
    # save stat to file
    print('orders stat is', orders_stat)
    file = open('st.txt', 'w')
    file.write(str(orders_stat))
    file.write(str(users_stat))
    file.close()
            
get_all_info() 
