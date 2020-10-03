from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView)


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user_registration/login.html'


class UserLogoutViews(LogoutView):
    template_name = 'user_registration/logged_out.html'


class UserPasswordResetFormView(PasswordResetView):
    email_template_name = 'user_registration/password_reset_email.html'
    template_name = 'user_registration/password_reset_form.html'
    success_url = reverse_lazy('user-password-reset-done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user_registration/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('user-password_reset_complete')
    template_name = 'user_registration/password_reset_confirm.html'


class UserResetPasswordComplet(PasswordResetCompleteView):
    template_name = 'user_registration/password_reset_complete.html'
