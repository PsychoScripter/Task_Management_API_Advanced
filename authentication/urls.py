from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ورود
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # تمدید

    path('register/', RegisterView.as_view(), name='register'),

]
