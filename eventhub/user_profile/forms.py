from django import forms
from eventhub.user_auth.models import AppUser
from eventhub.user_profile.models import Profile
from eventhub.helpers import BootstrapMixin

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()
        
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'description', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'date_of_birth': 'date of Birth',
            'description': 'Profile Description',
            'image': 'Profile Image',
        }
        widgets = {
           'first_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter first name',
               }
           ),
           'last_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter last name',
               }
           ),
           'description': forms.Textarea(
               attrs={
                   'placeholder': 'Enter description',
                   'rows': 3,
               }
           ),
           'date_of_birth': DateInput(
               attrs={
                   'min': '1920-01-01',
               }
           ),
    
        }
       
    def save(self, commit=True):
        profile = super().save(commit=commit)
        user = AppUser.objects.get(pk=profile.pk) 
        user.first_name = profile.first_name
        user.last_name = profile.last_name
                
        if commit:
            user.save()
        return profile

class UpdateProfileForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()
        
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'description', 'image')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'date_of_birth': 'date of Birth',
            'description': 'Profile Description',
            'image': 'Profile Image',
        }
        widgets = {
           'first_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter first name',
               }
           ),
           'last_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter last name',
               }
           ),
           'description': forms.Textarea(
               attrs={
                   'placeholder': 'Enter description',
                   'rows': 3,
               }
           ),
           'date_of_birth': DateInput(
               attrs={
                   'min': '1920-01-01',
               }
           ),
    
        }
    
    def save(self, commit=True):
        profile = super().save(commit=commit)
        user = AppUser.objects.get(pk=profile.pk) 
        user.first_name = profile.first_name
        user.last_name = profile.last_name
                
        if commit:
            user.save()
        return profile
    

class DeleteProfileForm(forms.ModelForm):
    pass
    