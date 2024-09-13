from django.urls import path # type: ignore
from .views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('api/register/', views.register, name='register'), # type: ignore
]
