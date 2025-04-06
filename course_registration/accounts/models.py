from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    
    def create(self,email,username=None,
                    password=None,
                    ):
       
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(
          
            email=self.normalize_email(email),
            username = username,
            # password=password,
            
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username=None,
                    password=None,
                    ):
       
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(
            # id=id,
            email=self.normalize_email(email),
            username = username,
            # password=password,

            is_admin=True,
            is_staff=True,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
 
class Accounts(AbstractBaseUser):
  
    username = models.CharField(max_length = 50,null=True)
    email = models.EmailField(max_length=100,unique=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Keeping Account status Active by default
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()
    
    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    class Meta:
        abstract = True

class Student(Accounts):
    class Meta:
        abstract = False

class Faculty(Accounts):
    class Meta:
        abstract = False