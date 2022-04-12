from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from eventhub.helpers import BootstrapMixin
from eventhub.user_profile.models import Profile

UserModel = get_user_model()

class UserRegistrationForm(BootstrapMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = False
        self._init__bootstrap_form_controls()
        
        
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Enter password',}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",  'placeholder': 'Re-enter password'}),
        strip=False,
        help_text=_(""),
    )
    
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email' )
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        
        widgets = {
           'first_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter first name',
                   'autofocus': True,
               }
           ),
           'last_name': forms.TextInput(
               attrs={
                   'placeholder': 'Enter last name',
               }
           ),
           'email': forms.TextInput(
               attrs={
                   'placeholder': 'Enter email',
               }
           ),
           'password1': forms.PasswordInput(
               attrs={
                   'placeholder': 'Enter password',
               }
           ),
           'password2': forms.PasswordInput(
               attrs={
                   'placeholder': 'Repeat password',
               }
           ),
    
        }
        

    
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.has_profile = True
        
        profile = Profile(
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            user=user,
        )
        
        if commit:
            profile.save()
            user.save()
            
        return user
    
class UserLogInForm(BootstrapMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()

class UserChangePasswordForm(BootstrapMixin, auth_forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()