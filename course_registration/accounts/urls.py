from django.urls import path,include
from .views import *

urlpatterns = [

    # Include Account Apis
    path('api/',include('accounts.apis.urls')),

]   
