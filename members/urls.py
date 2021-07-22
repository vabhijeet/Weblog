
from django.urls import path
from .views import UserRegisterView,UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(),name='register'),
    path('edit-profile/', UserEditView.as_view(),name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success,name='password_success'),
]
