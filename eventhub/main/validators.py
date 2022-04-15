from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Value must containt only letters!'
VALIDATE_ONLY_LETTERS_AND_SPACE_EXCEPTION_MESSAGE = 'Value must containt only letters and spaces!'
FILE_MAX_SIZE_EXCEPTION_MESSAGE = 'Max file size is '
ALLOWED_SYMBOLS = ['?', ' ', '.', '!', ',']

def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)

def only_letters_and_space_validator(value):
    for ch in value:
        if not ch.isalpha() and ch not in ALLOWED_SYMBOLS:
            raise ValidationError(VALIDATE_ONLY_LETTERS_AND_SPACE_EXCEPTION_MESSAGE)

@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size
    
    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())
    
    def __megabytes_to_bytes(self, value):
        return value * 1024 * 1024
    
    def __get_exception_message(self):
        return FILE_MAX_SIZE_EXCEPTION_MESSAGE + f'{self.max_size:.2f} MB!'