from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forgetPassword/', views.ForgetPassWordView.as_view(), name='forget_password_page'),
    path('activate-user/<email_active_code>', views.ActivateAccountView.as_view(), name='active-user'),
    path('set-password/<email_active_code>', views.SetPasswordView.as_view(), name='set-password'),
]
