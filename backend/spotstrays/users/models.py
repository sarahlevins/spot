from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, email, nickname, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.nickname = nickname
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, nickname, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.nickname = nickname
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, null=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname
