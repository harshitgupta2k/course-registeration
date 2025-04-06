from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from django.conf import settings
import jwt,datetime

from ..models import *
from ..serializers import *

from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404


# To be stored in django cache with expire duration
otp_container = {}

def get_user_email(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated')
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        email = payload.get('email')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Session Expired')
    return email


class OfferCourse(APIView):
    serializer_class=OfferCourseSerializer
    model = Course
    
    def get(self, request,format=None):

        email = get_user_email(request)
        queryset = self.model.objects.filter(faculty__email = email)

        serializer = CourseSerializer(queryset,many=True)

        return Response(serializer.data)
        
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):

            faculty = get_object_or_404(Faculty,email=get_user_email(request))
            try:
                
                course_object = serializer.save(
                    faculty=faculty
                    ) 
                return Response({'message':'course Added Succesfully.','id':course_object.code})
            except Exception as e:
                print(f"Exception occured while saving incident--{e}")
                return Response({'message':"Error try again later"})
        else:
            return Response({'message':serializer.errors})
        
class CourseRegistration(APIView):

    serializer_class=CourseRegisterationSerializer
    model = Registration
    
    def get(self, request,format=None):

        email = get_user_email(request)
        queryset = self.model.objects.filter(student__email = email)

        serializer = RegistrationSerializer(queryset,many=True)

        return Response(serializer.data)
        
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):

            student = get_object_or_404(Student,email=get_user_email(request))

            registered_courses = student.courses.filter(status = 'Pending').count()
            if registered_courses >= 2:
                return Response({'message':"can't enroll for more than 2 Pending Courses."}
                                ,status=status.HTTP_400_BAD_REQUEST)
            
            try:
                registration_object = serializer.save(
                    student=student
                    )
                return Response({'message':'Registration Succesfull.',})
            except Exception as e:
                print(f"Exception occured while saving incident--{e}")
                return Response({'message':"Error try again later"})
        else:
            return Response({'message':serializer.errors})