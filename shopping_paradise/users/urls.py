from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="user-login"),
    path('logout/', views.UserLogoutViews.as_view(), name="user-logout"),
    path('password_reset/', views.UserPasswordResetFormView.as_view(), name="user-password-reset"),
    path('password_reset/done', views.UserPasswordResetDoneView.as_view(), name="user-password-reset-done"),
    path('password_reset/complete', views.UserResetPasswordComplet.as_view(), name="user-password_reset_complete"),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='user-password_reset_confirm'),

]
