from accounts.models import User, UserProfile
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import  UniqueFieldsMixin, NestedUpdateMixin
from rest_framework import serializers, exceptions
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password
from django.db import IntegrityError, transaction
from djoser.conf import settings
import collections


class UserProfileSerializer(UniqueFieldsMixin, NestedUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model               = UserProfile
        fields              = ['__all__']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    phone_number = serializers.CharField()

    default_error_messages = {
        "cannot_create_user": 'unable to create User'
    }

    class Meta:
        model = User
        fields = ['id','email','phone_number', 'password']

    def validate(self, attrs):
        email=attrs['email']
        password=attrs['password']
        temp_attrs = collections.OrderedDict(email=email, password=password)
        user = User(**temp_attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        phone_number = validated_data['phone_number']
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        UserProfile.objects.create(user=user, phone_number=phone_number)

        return user


class UserSerializer(UniqueFieldsMixin, NestedUpdateMixin, serializers.ModelSerializer):
    userprofile = UserProfileSerializer
    class Meta:
        model = User
        fields = ['id','email','userprofile']
        depth = 1
        read_only_fields = (settings.LOGIN_FIELD,)
        ref_name = "my users"
