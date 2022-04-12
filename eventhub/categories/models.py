from django.db import models
from eventhub.categories.validators import MaxFileSizeInMbValidator, only_letters_validator
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Category(models.Model):
    ONLY_LETTERS_VALIDATOR = only_letters_validator
    
    CATEGORY_TYPE_MIN_LEN = 2
    CATEGORY_TYPE_MAX_LEN = 15
    
    CATEGORY_DESCRIPTION_MIN_LEN = 5
    CATEGORY_DESCRIPTION_MAX_LEN = 35

    IMAGE_MAX_SIZE_IN_MB = 2
    IMAGE_UPLOAD_TO_DIR = 'categories/'
    
    category_type = models.CharField(
        max_length=CATEGORY_TYPE_MAX_LEN,
        unique=True,
        validators=(
            MinLengthValidator(CATEGORY_TYPE_MIN_LEN),
            MaxLengthValidator(CATEGORY_TYPE_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        )
    )
    
    category_description = models.CharField(
        max_length=CATEGORY_DESCRIPTION_MAX_LEN,
        validators=(
            MinLengthValidator(CATEGORY_DESCRIPTION_MIN_LEN),
            MaxLengthValidator(CATEGORY_DESCRIPTION_MAX_LEN),
            ONLY_LETTERS_VALIDATOR,
        )
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
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
    
    def __str__(self) -> str:
        return f'{self.category_type}'