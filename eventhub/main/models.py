from django.db import models
from eventhub.categories.models import Category
from eventhub.categories.validators import MaxFileSizeInMbValidator, only_letters_validator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import get_user_model
from cloudinary import models as cloudinary_models

UserModel = get_user_model()

class Home(models.Model):
    
    home_skin = models.CharField(
        max_length= 15,
        default=''
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    
    topic_first_message = models.CharField(
        max_length= 26,
        default='',
    )
    
    topic_second_message = models.CharField(
        max_length= 26,
        default='',
    )
    
    topic_third_message = models.CharField(
        max_length= 26,
        default='',
    )
    
    welcome_message = models.TextField(
        max_length= 256,
        default='',
    )
    
    first_message = models.TextField(
        max_length= 256,
        default='',
    )
    
    second_message = models.TextField(
        max_length= 256,
        default='',
    )
    
    third_message = models.TextField(
        max_length= 256,
        default='',
    )
    

class Event(models.Model):
    ONLY_LETTERS_VALIDATOR = only_letters_validator
    
    EVENT_TOPIC_MIN_LEN = 2
    EVENT_TOPIC_MAX_LEN = 15
    
    EVENT_BRIEF_DESCRIPTION_MIN_LEN = 5
    EVENT_BRIEF_DESCRIPTION_MAX_LEN = 100

    IMAGE_MAX_SIZE_IN_MB = 2
    IMAGE_UPLOAD_TO_DIR = 'events/'
    
            
    
    topic = models.CharField(
        max_length=EVENT_TOPIC_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(EVENT_TOPIC_MIN_LEN),
            MaxLengthValidator(EVENT_TOPIC_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        )
    )
    
    
    brief_description = models.CharField(
        max_length=EVENT_BRIEF_DESCRIPTION_MAX_LEN,
        validators=(
            MinLengthValidator(EVENT_BRIEF_DESCRIPTION_MIN_LEN),
            MaxLengthValidator(EVENT_BRIEF_DESCRIPTION_MAX_LEN),
        )
    )
    
    description = models.TextField(
        null=True,
        blank=True,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    
    image = cloudinary_models.CloudinaryField('image', blank = True, null = True)
    
    # image = models.ImageField(
    #     upload_to=IMAGE_UPLOAD_TO_DIR,
    #     null=True,
    #     blank=True,
    #     validators=(
    #         MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
    #     )
    # )
    
    user = models.ForeignKey(
        UserModel,#user_profile pints to Profile table
        on_delete=models.CASCADE,
    )
    
    category = models.ForeignKey(
        Category,#user_profile pints to Profile table
        on_delete=models.CASCADE,
    )
    
    # def delete(self, *args, **kwargs):
    #     image_dir = self.image
    # You have to prepare what you need before delete the model
        # if image_dir:
        #     storage, path = self.image.storage, self.image.path
    # Delete the model before the file
        # super(Event, self).delete(*args, **kwargs)
    # Delete the file after the model
        # if image_dir:
        #     storage.delete(path)



class Comment(models.Model):
    
    text = models.TextField(
        null=True,
        blank=True,
    )
    
    user = models.ForeignKey(
        UserModel,#user_profile pints to Profile table
        on_delete=models.CASCADE,
    )
    
    event = models.ForeignKey(
        Event,#user_profile pints to Profile table
        on_delete=models.CASCADE,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )