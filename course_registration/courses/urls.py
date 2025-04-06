from django.urls import path,include
from .views import *

urlpatterns = [

    # Include Account Apis
    path('api/',include('courses.apis.urls')),

]   
