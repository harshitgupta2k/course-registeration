
from rest_framework import serializers
from .models import  *
import re

# password validator 
def validate(self,attrs):
        
    password = attrs.get('password')

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[a-zA-Z\d\W]{8,}$"

    if 'confirm_password' in attrs and password != attrs['confirm_password']:
        raise serializers.ValidationError("Passwords do not match.")

    if re.match(pattern, password):
        attrs.pop('confirm_password', None)
        return attrs
    else:
        raise serializers.ValidationError("Password Must be 8 characters Long, contains at least 1 x (upper, lower, number and special character.)")


# --------------------       Students       -----------------------

class Student_sign_up_serializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(min_length = 8, max_length = 68, write_only=True)

    class Meta:
        model = Student
        fields = ('username','email',
                'password','confirm_password',
                )
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    validate = validate



# --------------------       Faculty      -----------------------

class Faculty_sign_up_serializer(Student_sign_up_serializer):
    class Meta:
        model = Faculty
        fields = ('username','email',
                'password','confirm_password',
                )
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    validate = validate
