from django.contrib import admin
from eventhub.user_profile.models import Profile
from django import forms

# Register your models here.

class ProfileForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'description', 'image', 'user')
       
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', )
    form = ProfileForm
    
    def save_related(self, request, form, formsets, change):
        super(ProfileAdmin, self).save_related(request, form, formsets, change)
        obj = form.instance
        user = obj.user
        user.first_name = obj.first_name
        user.last_name = obj.last_name
        user.has_profile = True
        user.save()

admin.site.register(Profile, ProfileAdmin)