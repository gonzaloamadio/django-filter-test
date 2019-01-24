from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .forms import UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('email', 'user_type', 'is_active')
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password', 'user_type', 'date_joined')},
        ),
        #        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        #        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'user_type'),
            },
        ),
    )
    search_fields = ('email', 'user_type')
    ordering = ('email',)
    save_on_top = True
    readonly_fields = ["date_joined", "is_staff", "is_superuser"]
