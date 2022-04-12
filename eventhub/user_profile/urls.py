from django.urls import path
from eventhub.user_profile.views import  DeleteProfileView, CreateProfileView, DetailsProfileShortView, UpdateProfileView, DetailsProfileView, profile_delete_page# profile_create_page, profile_edit_page, profile_details_page, 


urlpatterns = [
    path('details/<int:pk>/', DetailsProfileView.as_view(), name='profile_details'),
    path('details/short/<int:pk>/', DetailsProfileShortView.as_view(), name='profile_details_short'),
    path('create/', CreateProfileView.as_view(), name='profile_create'),
    path('update/<int:pk>/', UpdateProfileView.as_view(), name='profile_update'),
    path('delete_page/', profile_delete_page, name='profile_delete_page'),
    path('delete/<int:pk>/', DeleteProfileView.as_view(), name='profile_delete'),
]