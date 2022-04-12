from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from eventhub.user_auth.views import UserLoginView, UserLogoutView, UserRegistrationView , user_logout_page, UserChangePasswordView #user_login_page, user_register_page

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('logout_page/', user_logout_page, name='user_logout_page'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('change_password/', UserChangePasswordView.as_view(), name='user_change_password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('home')), name='password_change_done')
]