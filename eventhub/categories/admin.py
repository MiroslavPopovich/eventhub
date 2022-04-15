from django.contrib import admin
from eventhub.categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_type', 'category_description')