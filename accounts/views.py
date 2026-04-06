from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, CreateAPIView,ListAPIView
from rest_framework.response import Response

from accounts.serializers import RegisterSerializer
User = get_user_model()

class UserRegisterListApiViews(ListCreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        serializer.save()