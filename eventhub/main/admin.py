from django.contrib import admin
from eventhub.main.models import Home
from django import forms

# Register your models here.
class HomeForm(forms.ModelForm):
        
    class Meta:
        model = Home
        fields = ('home_skin', 
                  'welcome_message',
                  'topic_first_message', 'first_message',
                  'topic_second_message', 'second_message',
                  'topic_third_message', 'third_message',)
       
    
class HomeAdmin(admin.ModelAdmin):
    list_display = ('home_skin', 'created_at')
    form = HomeForm
    
    def save_model(self, request, obj, form, change):
        obj.__class__.objects.all().delete()
        super().save_model(request, obj, form, change)
    

admin.site.register(Home, HomeAdmin)
