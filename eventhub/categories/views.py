from django.shortcuts import render
from django.views import generic as views
from django.core.paginator import Paginator

from eventhub.categories.models import Category
from eventhub.main.models import Event

class CategoriesView(views.ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

class DashboardByCategoriesView(views.DetailView):
    model = Category
    template_name = 'dashboard_by_category.html'
    context_object_name = 'category'
   
    
    def get_context_data(self, **kwargs):
        context =  super(DashboardByCategoriesView, self).get_context_data(**kwargs)
        current_category = self.object
        request = self.request
        events = current_category.event_set.all()
        
        page_number = request.GET.get('page')
        paginator = Paginator(events, 4) # 4 objects per page
        page_obj = paginator.get_page(page_number)
        
        categories = list(Category.objects.all()) #.values_list('category_type', flat=True)
        context.update({
            'current_category': current_category,
            'events': page_obj, #takes only the events related to the current page if all are needed use events insted
            'categories': categories,
            'page_obj': page_obj,
        })
        return context
    

