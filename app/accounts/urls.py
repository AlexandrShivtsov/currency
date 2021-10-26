from accounts.views import ActivateUserView, MyProfileView, SingUpView

from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView


app_name = 'accounts'
urlpatterns = [

    path('login/', RedirectView.as_view(url='http://127.0.0.1:8000/')),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('sing-up/', SingUpView.as_view(), name='sing-up'),
    path('activate/<uuid:username>', ActivateUserView.as_view(), name='activate-user'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
