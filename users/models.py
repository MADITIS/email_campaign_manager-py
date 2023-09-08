from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from campaigns.models import Campaign


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        # if password is None:
        #     raise ValueError('The Password field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_campaigns = models.ManyToManyField(Campaign)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
