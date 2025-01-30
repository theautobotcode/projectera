from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
import os
from django.template.loader import render_to_string

from organizations.models import Organization


class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser."""
    
    def create_user(self, email, phone_number, password=None, **extra_fields):
        """Create and return a regular user."""
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', "superadmin")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, phone_number, password, **extra_fields)


class AbstractBaseUserWithProfile(AbstractBaseUser, PermissionsMixin):
    """Abstract base user model with additional fields."""
    
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.CharField(max_length=255, blank=True, null=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
    )
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    class Meta:
        abstract = True

class User(AbstractBaseUserWithProfile):
    """Concrete user model inheriting from the abstract base user."""

    ROLES = [
        ('superadmin', 'Super Admin'),
        ('backend', 'Backend'),
        ('org-admin', 'Admin'),
        ('org-operator', 'Operator'),
    ]
    
    role = models.CharField(max_length=50, choices=ROLES, default='org-operator')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return str(self.email)

html_msg='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Created Successfully</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            background: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        p {
            font-size: 16px;
            color: #333;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            margin-top: 20px;
            background: #4CAF50;
            color: #ffffff;
            text-decoration: none;
            font-size: 16px;
            border-radius: 5px;
        }
        .footer {
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }
        .thank-you {
            margin-top: 30px;
            font-weight: bold;
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Congratulations! 🎉</h1>
        <p>Dear <strong>{{ user_name }}</strong>,</p>
        <p>Your account has been successfully created! Welcome to our community.</p>
        <p>Click the button below to log in and start exploring.</p>
        <a href="{{ login_url }}" class="button">Login to Your Account</a>

        <p class="thank-you">Thank you for joining us!  
        <br>– The Project Era Team 🚀</p>

        <p class="footer">If you did not sign up, please ignore this email or contact support.</p>
    </div>
</body>
</html>

'''
@receiver(post_save,sender=User)
def user_creation(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Congratulation ! Your Account has been created.",
            message=render_to_string(html_msg),
            from_email=os.getenv("EMAIL_HOST_USER",""),
            recipient_list= [instance.email, ],
            fail_silently=True
        )
