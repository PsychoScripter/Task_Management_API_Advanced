from rest_framework import generics
from authentication.models import CustomUser


from authentication.serializers import UserRegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
