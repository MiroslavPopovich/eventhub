from django.shortcuts import render
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.views import generic as views
from eventhub.user_auth.forms import UserLogInForm, UserRegistrationForm, UserChangePasswordForm

class UserLoginView(auth_views.LoginView):
    form_class = UserLogInForm
    template_name = 'user_login.html'
    success_url = reverse_lazy('home')
    
    def get_success_url(self):   
        if self.success_url:
            return self.success_url
        return super().get_success_url()
       
    
class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result

def user_logout_page(request):
    context = {
    }
    return render(request=request, template_name='user_logout.html', context=context)

class UserLogoutView(auth_views.LogoutView):
    #template_name = 'home.html'
    pass

class UserChangePasswordView(auth_views.PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'user_change_password.html'