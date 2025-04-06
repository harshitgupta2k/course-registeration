
from rest_framework import serializers
from .models import  *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class OfferCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name',)



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class CourseRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('course',)
