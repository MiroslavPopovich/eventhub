from datetime import datetime
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import get_user_model
from eventhub.user_profile.validators import MaxFileSizeInMbValidator, only_letters_validator

from django.db.models.signals import post_delete
from django.dispatch import receiver

UserModel = get_user_model()
class Profile(models.Model):
    
    ONLY_LETTERS_VALIDATOR = only_letters_validator
    
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    
    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]
    
    IMAGE_MAX_SIZE_IN_MB = 2
    IMAGE_UPLOAD_TO_DIR = 'profiles/'
    
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            MaxLengthValidator(FIRST_NAME_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        )
    )
    
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            MaxLengthValidator(LAST_NAME_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        )
    )

    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    
    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        )
    )
    
    description = models.TextField(
        null=True,
        blank=True,
    )
      
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    def delete(self, *args, **kwargs):
        image_dir = self.image
    # You have to prepare what you need before delete the model
        if image_dir:
            storage, path = self.image.storage, self.image.path
    # Delete the model before the file
        super(Profile, self).delete(*args, **kwargs)
    # Delete the file after the model
        if image_dir:
            storage.delete(path)
    
    @property
    def age(self):
        return datetime.now().year - self.date_of_birth.year
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

@receiver(post_delete, sender=Profile)
def auto_delete_appuser_with_profile(sender, instance, **kwargs):
    instance.user.delete()

