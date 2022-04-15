from django import forms
from eventhub.helpers import BootstrapMixin
from eventhub.main.models import Comment, Event

class CreateEventForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()
        
    class Meta:
        model = Event
        fields = ('topic', 'category', 'brief_description', 'description', 'image') #
        labels = {
            'topic': 'Event Topic',
            'category': 'Event Category',
            'brief_description': 'Brief Event Description',
            'description': 'Event Description',
            'image': 'Event Image',
        } 
        widgets = {
           'topic': forms.TextInput(
               attrs={
                   'placeholder': 'Enter event Topic',
               }
           ),
           'brief_description': forms.TextInput(
               attrs={
                   'placeholder': 'Enter brief event description',
               }
           ),
           'description': forms.Textarea(
               attrs={
                   'placeholder': 'Enter event description',
                   'rows': 3,
               }
           ),
    
        }
        
class UpdateEventForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()
        
    class Meta:
        model = Event
        fields = ('topic', 'category', 'brief_description', 'description', 'image') #
        labels = {
            'topic': 'Event Topic',
            'category': 'Event Category',
            'brief_description': 'Brief Event Description',
            'description': 'Event Description',
            'image': 'Event Image',
        } 
        widgets = {
           'topic': forms.TextInput(
               attrs={
                   'placeholder': 'Enter event Topic',
               }
           ),
           'brief_description': forms.TextInput(
               attrs={
                   'placeholder': 'Enter brief event description',
               }
           ),
           'description': forms.Textarea(
               attrs={
                   'placeholder': 'Enter event description',
                   'rows': 3,
               }
           ),
    
        }

class CommentEventForm(BootstrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._init__bootstrap_form_controls()
        
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': '',
            
        } 
        widgets = {
           'text': forms.Textarea(
               attrs={
                   'placeholder': 'Enter your comment',
               }
           ),   
        }
    
    
