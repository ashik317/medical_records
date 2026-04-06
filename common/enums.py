from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRoleChoices(models.TextChoices):
    ADMIN = 'ADMIN', _('Admin')
    DOCTOR = 'DOCTOR', _('Doctor')
    NURSE = 'NURSE', _('Nurse')
    RECEPTIONIST = 'RECEPTIONIST', _('Receptionist')
    PATIENT = 'PATIENT', _('Patient')

class GenderChoices(models.TextChoices):
    MALE = 'MALE', _('Male')
    FEMALE = 'FEMALE', _('Female')
    OTHER = 'OTHER', _('Other')
