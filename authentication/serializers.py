from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
