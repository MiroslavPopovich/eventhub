from django.db import models
from django.contrib.auth import models as auth_models
from eventhub.user_auth.managers import AppUsersManager
from eventhub.user_profile.validators import MaxFileSizeInMbValidator, only_letters_validator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    
    ONLY_LETTERS_VALIDATOR = only_letters_validator
    
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    
    first_name = models.CharField(
        default='',
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            MaxLengthValidator(FIRST_NAME_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        ),
        
    )
    
    last_name = models.CharField(
        default='',
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            MaxLengthValidator(LAST_NAME_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        ),
    )
    
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    
    has_profile = models.BooleanField(
        default=False,
    )
    
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    
    is_active = models.BooleanField(default=True)
   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = AppUsersManager()

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin