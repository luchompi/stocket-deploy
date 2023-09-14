from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group

class UserAccountManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Los usuarios deben tener un correo')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email,password,**extra_fields)


class UserAccount(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    city = models.CharField(max_length=255, default='Riohacha')
    uid = models.CharField(max_length=255,unique=True,null=True,blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="user_groups")
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.username