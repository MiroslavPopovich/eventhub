from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy
from eventhub.categories.models import Category

from eventhub.main.forms import CreateEventForm, UpdateEventForm, CommentEventForm
from eventhub.main.models import Event, Home, Comment

class HomeView(views.TemplateView):
    model = Home
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context =  super(HomeView, self).get_context_data(**kwargs)
        
        home_skin = list(Home.objects.all())
        if len(home_skin) > 0:
             home_skin = list(Home.objects.all())[0]
        else:
            home_skin = Home(welcome_message='No Data1',
                             first_message='No Data2.1',
                             second_message='No Data3.1',
                             third_message='No Data4.1',
                             topic_first_message='No Data2',
                             topic_second_message='No Data3',
                             topic_third_message='No Data4'
                             )
        
        context.update({
            'home_skin': home_skin,
        })
        return context
    
    
class DashboardView(views.ListView):
    model = Event
    template_name = 'dashboard.html'
    context_object_name = 'events'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        categories = list(Category.objects.all()) #.values_list('category_type', flat=True)
        context.update({
            'categories': categories,
        })
        return context
    


class CreateEventView(views.CreateView):
    template_name = 'event_create.html'
    form_class = CreateEventForm
    def get_success_url(self):
        #pk=self.object.user.pk
        #return reverse_lazy('profile_details', kwargs={'pk': pk})
        return reverse_lazy('dashboard')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class UpdateEventView(views.UpdateView):
    model = Event
    template_name = 'event_update.html'
    form_class = UpdateEventForm
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        previous_url = self.request.META.get('HTTP_REFERER')
        context.update({
            'previous_url': previous_url,
        })
        return context
    
    def get_success_url(self):
        pk=self.object.pk
        return reverse_lazy('event_details', kwargs={'pk': pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteEventView(views.DeleteView):
    model = Event
    template_name = 'event_delete.html'
    
    def get_success_url(self):
        pk=self.object.user.pk
        return reverse_lazy('profile_details', kwargs={'pk': pk})


class DetailsEventView(views.edit.FormMixin, views.DetailView):
    model = Event
    template_name = 'event_details.html'
    context_object_name = 'event'
    form_class = CommentEventForm
    
    def get_context_data(self, **kwargs):
        context =  super(DetailsEventView, self).get_context_data(**kwargs)
        form = CommentEventForm(initial={'post': self.object})
        categories = list(Category.objects.all())
        current_event = self.object
        comments = current_event.comment_set.all()
        all_comments = len(comments)
        can_delete_comments = self.request.user.has_perm('main.delete_comment')
        context.update({
            'form': form,
            'comments': comments,
            'all_comments': all_comments,
            'categories': categories,
            'can_delete_comments': can_delete_comments,
        })
        return context
    
    def get_success_url(self):
          pk=self.kwargs['pk']
          return reverse_lazy('event_details', kwargs={'pk': pk})
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        form.instance.event = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
  
    
    
def event_delete_page(request, pk):
    previous_url = request.META.get('HTTP_REFERER')
    context = {
        'event_pk': pk,
        'previous_url': previous_url, 
    }
    return render(request=request, template_name='event_delete.html', context=context)

def comment_delete_page(request, pk):
    previous_url = request.META.get('HTTP_REFERER')
    context = {
        'comment_pk': pk,
        'previous_url': previous_url, 
    }
    return render(request=request, template_name='comment_delete.html', context=context)

class DeleteCommentView(views.DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    
    def get_success_url(self):
        pk=self.object.event.pk
        return reverse_lazy('event_details', kwargs={'pk': pk})

def handler404(request, exception):
    return render(request=request, template_name='page_not_found.html')