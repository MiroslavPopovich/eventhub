from django.urls import path
from eventhub.main.views import HomeView, DashboardView, CreateEventView, UpdateEventView, DeleteEventView, DeleteCommentView, DetailsEventView,  event_delete_page, comment_delete_page

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/create/', CreateEventView.as_view(), name='event_create'),
    path('event/edit/<int:pk>/', UpdateEventView.as_view(), name='event_update'),
    path('event/delete/<int:pk>/', DeleteEventView.as_view(), name='event_delete'),
    path('event/delete_page/<int:pk>/', event_delete_page, name='event_delete_page'),
    path('event/delete/comment_page/<int:pk>/', comment_delete_page, name='comment_delete_page'),
    path('event/delete/comment/<int:pk>/', DeleteCommentView.as_view(), name='comment_delete'),
    path('event/<int:pk>/', DetailsEventView.as_view(), name='event_details'),
]