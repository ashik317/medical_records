from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from accounts.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'alias',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'password',
            'password2',
            'role',
            'phone',
            'gender',
            'date_of_birth',
            'address',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]
        read_only_fields = [
            'alias',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        validated_data.pop("password2", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        validated_data.pop("password2", None)  # remove if present

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = [
            'alias',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'phone',
            'gender',
            'date_of_birth',
            'address',
            'profile_picture',
            'created_at'
            'updated_at',
            'created_by',
            'updated_by',
        ]
        read_only_fields = [
            'alias',
            'created_at'
            'updated_at',
            'created_by',
            'updated_by',
        ]

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["confirm_password"] != attrs["new_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()