from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'password-reset/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path(
        'confirm-email/<str:key>/', TemplateView.as_view(),
        name='account_confirm_email_custom'
    ),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]
