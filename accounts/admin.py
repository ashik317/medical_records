from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display      = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_superuser', 'is_active')
    list_filter       = ('role', 'is_staff', 'is_superuser', 'is_active', 'gender')
    search_fields     = ('email', 'first_name', 'last_name', 'phone')
    ordering          = ('email',)
    filter_horizontal = ('groups', 'user_permissions')

    readonly_fields = (
        'last_login',
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
        'alias',
        'user_ip',
    )

    fieldsets = (
        ('Login Info',    {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'phone', 'date_of_birth', 'gender', 'address', 'profile_picture')}),
        ('Role',          {'fields': ('role', 'is_verified')}),
        ('Permissions',   {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Timestamps',    {'fields': ('last_login', 'created_at', 'updated_at', 'created_by', 'updated_by', 'alias', 'user_ip')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':  ('email', 'first_name', 'last_name', 'role', 'password1', 'password2'),
        }),
    )

    def save_model(self, request, obj, form, change):
        # set created_by and updated_by automatically
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        # skip full_clean to avoid admin validation conflicts
        obj.user_ip = request.META.get('REMOTE_ADDR', '')
        super(BaseUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)