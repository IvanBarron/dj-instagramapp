from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'website', 'picture' )
    list_display_links = ('id', 'user')
    list_aditable = ('phone_nmber', 'website', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('created_at', 'modified_at')

    fieldsets = (
        ("Profile", {
            "fields": (
                ("user", "picture")
            ),
        }),
        ("Extra Info",
        {
            "fields":(
                "website", "biography"
            )
        }),
    )


class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete = False
    verbose_name_plural = "Profiles"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    