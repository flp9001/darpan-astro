import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
        is_staff=is_staff, is_active=True,
        is_superuser=is_superuser, last_login=now,
        date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
         
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
        
        
class User(AbstractBaseUser, PermissionsMixin):
    
    username_validator = UnicodeUsernameValidator()
    
    username = models.CharField(_("username"), max_length=15, unique=True, 
        help_text=_("Required. 15 characters or fewer. Letters, \ numbers and @/./+/-/_ characters"), 
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
            },
        )

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False, help_text=_('Designates whether this user has confirmed his account.'))
    
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
        
    def get_short_name(self):
        return self.first_name
        
    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])