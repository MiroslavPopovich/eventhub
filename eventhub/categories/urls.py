from django.urls import path
from eventhub.categories.views import CategoriesView, DashboardByCategoriesView

urlpatterns = [
    path('', CategoriesView.as_view(), name='categories'),
    path('dashboard/category/<int:pk>/', DashboardByCategoriesView.as_view(), name='dashboard_by_category'),
]