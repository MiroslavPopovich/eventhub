from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from eventhub.user_profile.forms import  DeleteProfileForm, UpdateProfileForm, CreateProfileForm
from eventhub.user_profile.models import Profile

class CreateProfileView(views.CreateView):
    
    template_name = 'profile_create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        current_user = self.request.user
        current_user.has_profile = True
        current_user.save()
        form.instance.user = current_user
        form.save()
        return super().form_valid(form)
    
    
class UpdateProfileView(views.UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    form_class = UpdateProfileForm
    def get_success_url(self):
          pk=self.kwargs['pk']
          return reverse_lazy('profile_details', kwargs={'pk': pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profile_delete.html'
    #form_class = DeleteProfileForm
    success_url = reverse_lazy('home')
    
    

class DetailsProfileView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        profile = self.object
        events = profile.user.event_set.all()
        total_events = len(events)
        context.update({
            'profile': profile,
            'is_owner': self.object.user_id == self.request.user.id,
            'events': events,
            'total_events': total_events
        })
        return context


class DetailsProfileShortView(views.DetailView):
    model = Profile
    template_name = 'profile_details_short.html'
    context_object_name = 'profile'
    
    @method_decorator(login_required(login_url='/user/login/'))
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)
    
def profile_delete_page(request):
    context = {
    }
    return render(request=request, template_name='profile_delete.html', context=context)

