from django.urls import path
from store.views import *

urlpatterns = [
    path('', index, name='index'),
    
    
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),


    path('orders/', orders, name='orders'),
    path('profile/', profile, name='profile'),


    # path('register/', register, name='register'),
    # path('login/', login, name='login'),
    # path('logout/', logout, name='logout'),

    
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
]