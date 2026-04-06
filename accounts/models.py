from django.db import models
from common.enums import (
    UserRoleChoices,
    GenderChoices
)
from common.models import CreatedAtUpdatedModel

class User(CreatedAtUpdatedModel):
    fast_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserRoleChoices.choices,
        null=True,
        blank=True
    )
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, blank=True, null=True)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fast_name} ({self.role})"

    def get_full_name(self):
        return f"{self.fast_name} {self.middle_name} {self.last_name}"
