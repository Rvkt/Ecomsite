from django.urls import path
from ap.views import *


urlpatterns = [
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),
]
