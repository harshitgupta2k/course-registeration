from django.urls import path
from .views import *

urlpatterns = [

    # Basic Account Management URLs

    path('sign_up/<user_type>/',SignUp.as_view(),name="sign_up_api"),

    path('login/<user_type>/',login,name="login_api"),

    path('logout/',logout,name="logout_api"),

]
