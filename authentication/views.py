from rest_framework import generics
from authentication.models import CustomUser
from rest_framework.permissions import AllowAny

from authentication.serializers import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
