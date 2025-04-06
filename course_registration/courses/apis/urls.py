from django.urls import path
from .views import *

urlpatterns = [

    # Basic Account Management URLs

    path('offer/',OfferCourse.as_view(),name="offer_course_api"),

    path('registeration/',CourseRegistration.as_view(),name="course_registration_api"),

]
