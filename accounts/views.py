from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import RegisterSerializer
User = get_user_model()

class UserListApiView(ListAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "phone",
        "role",
        "date_of_birth",
    ]
    def get_queryset(self):
        return User.objects.all()


class UserRegisterListApiView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class UserDetailApiView(RetrieveUpdateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = "alias"

    def get_object(self):
        return User.objects.get(
            alias=self.kwargs['alias']
        )

    def perform_update(self, serializer):
        serializer.save()