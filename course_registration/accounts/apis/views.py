from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from django.conf import settings
import jwt,datetime

from ..models import *
from ..serializers import *


class SignUp(APIView):

    # Just For DRF Form View in browser
    serializer_class = Student_sign_up_serializer

    def post(self,request,user_type):

        if user_type == 'student':
            self.serializer_class = Student_sign_up_serializer
        elif user_type == 'faculty':
            self.serializer_class = Faculty_sign_up_serializer
        else:
            return Response({"message":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        serializer_object = self.serializer_class(data=data)
        if serializer_object.is_valid():
            try:
                serializer_object.save()
                return Response({'message':"success",'user':serializer_object.data},status=status.HTTP_200_OK)
            except Exception as e:
                print("Exception occured ----",e)
                return Response({"message":e},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':serializer_object.errors}, status=status.HTTP_400_BAD_REQUEST)  


@api_view(("POST",))
def login(request,user_type):

    model = ''

    if user_type == 'student':
        model = Student
    elif user_type == 'faculty':
        model = Faculty
    else:
        return Response({"message":"Invalid Request"},status=status.HTTP_400_BAD_REQUEST)

    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = model.objects.get(email=email)
    except model.DoesNotExist:
        return Response({'error':'Account Does Not Exist.'}) 
    except Exception as e:
        print("Error occured while logging in --",e)
        return Response({'error':'Something went wrong'}) 
    
    if user.is_active:
        valid_password = user.check_password(password)
        if valid_password:
            pass
        else:
            return Response({'error':'Incorrect password'})
    else:
        return Response({'error':'Your account is not activated yet.'}) 
    
    payload = {
                'email':user.email,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=48),
                'iat' : datetime.datetime.utcnow()
                }
                    
    # Creating a token for logged in user for authentication purpose which will remain valid upto 2 days
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')

    user_data = {
        'name' : user.username,
    }

    response = Response(status=status.HTTP_200_OK)

    # Setting the token in user's browser cookie
    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data = {'message':f"Login Success",
                     'user':user_data,
                     }
    return response


@api_view(("POST",))
def logout(request):
    try:
        token = request.COOKIES['jwt']
    except:
        return Response({"Error":f"Please Login Again."},status=status.HTTP_401_UNAUTHORIZED)
    response = Response()
    response.delete_cookie('jwt')
    response.data = {'Success':"Log out success"}
    return response
