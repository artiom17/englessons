from django.urls import path
from . import views
from .views import VerificationView, SetNewPasswordView, RequestResetEmailView

urlpatterns = [
    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('set-new-password/<uidb64>/<token>', SetNewPasswordView.as_view(), name="set-new-password"),
    path('request-reset-email', RequestResetEmailView.as_view(), name="request-reset-email"),
]
