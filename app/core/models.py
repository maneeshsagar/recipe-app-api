
from django.db import models
from django.contrib.auth.models import UserManager , AbstractBaseUser ,\
     BaseUserManager , PermissionsMixin
from django.db.models.base import Model
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        """creates and saves the user"""
        if not email:
            raise ValueError('User must have email address')
        user=self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_super_user(self,email,password):
        """Creates SuperUser"""
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model that supoorts email instead of the username"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    objects=UserManager()