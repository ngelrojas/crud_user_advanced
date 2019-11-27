from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
            (None, {'fields': ('email', 'password')}),
            (_('Personal Info'),
                {
                    'fields': (
                        'name',
                        'last_name',
                        'dni',
                        'cellphone',
                        'address',
                        'photo',
                        'type_user',
                        'created_at',
                    )
                }),
            (
                _('Permissions'),
                {
                    'fields': ('is_active', 'is_staff', 'is_superuser')
                }
            ),
            (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')}),
        )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.CodeActivation)
admin.site.register(models.Biography)
admin.site.register(models.Campaing)
admin.site.register(models.TagCampaing)
admin.site.register(models.CategoryCampaing)
admin.site.register(models.Reward)
admin.site.register(models.Payment)
admin.site.register(models.Like)
admin.site.register(models.Comment)
admin.site.register(models.SubComment)
admin.site.register(models.Currency)
