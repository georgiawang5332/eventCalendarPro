from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    """ User manager """

    def _create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        """使用電子郵件地址創建並返回新用戶"""
        if not email:  # check for an empty email/檢查電子郵件是否為空
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email/規範化提供的電子郵件
            email = self.normalize_email(email)

        # create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        """使用電子郵件地址創建並返回新用戶"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        """使用電子郵件地址創建並返回新的員工用戶"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """  """自定義用戶模型"""

    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
        help_text="Ex: example@example.com",
    )

    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)


    is_staff = models.BooleanField(_("Staff status"), default=False)
    is_active = models.BooleanField(_("Active"), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    last_updated = models.DateTimeField(_("Last Updated"), auto_now=True)

    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


# User(email=email, otherfields)
