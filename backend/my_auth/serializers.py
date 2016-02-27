from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'username',

        )
        read_only_fields = (
            'username',
        )

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    default_error_messages = {
            'inactive_account': 'User account is disabled.',
        'invalid_credentials': 'Unable to login with provided credentials.',
    }

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.user = None
        self.fields['username'] = serializers.CharField(required=True)

    def validate(self, attrs):
        self.user = authenticate(username=attrs['username'], password=attrs['password'])
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = (
            'auth_token',
        )