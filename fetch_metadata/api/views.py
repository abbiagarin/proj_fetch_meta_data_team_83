from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import get_user_model,views
from .forms import SignupForm,CustomUserLoginForm,ChangePasswordForm, PasswordResetForm
from django.contrib.auth.forms import AuthenticationForm
from .permissions import IsCreatorOrAdminReadOnly
from . import serializers



# Create your views here.

UserModel = get_user_model()

class CreateUserView(CreateView):
    template_name = 'api/signup.html'
    model = UserModel
    form_class = SignupForm
    success_url = '/login/'

class LoginUserView(views.LoginView):
    template_name = 'api/login.html'
    model = UserModel
    form_class = AuthenticationForm
    next_page = '/<user>/dashboard/'

class UserPasswordChangeView(views.PasswordChangeView):
    template_name = 'api/password_change.html'
    model = UserModel
    form_class = ChangePasswordForm

class UserResetPasswordView(views.PasswordResetView):
    template_name='api/password_reset.html'
    model = UserModel
    form_class = PasswordResetForm
