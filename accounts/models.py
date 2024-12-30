from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models
from django.utils.timezone import now

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
        'Organization', on_delete=models.SET_NULL, null=True, blank=True, related_name='users'
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
        return self.email
